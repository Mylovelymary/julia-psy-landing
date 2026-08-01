'use client';

import React, { useState, useEffect, useCallback, useRef } from 'react';

const triggers = [
  'А вдруг...',
  'Я не справлюсь',
  'Все смотрят',
  'Я не успеваю',
  'Опасно',
  'Что они подумают?'
];

export default function ThoughtCatcher() {
  const [thoughts, setThoughts] = useState([]);
  const [score, setScore] = useState(0);
  const [isGameOver, setIsGameOver] = useState(false);
  const containerRef = useRef(null);

  // Функции для получения случайных координат
  const getRandomPosition = () => {
    if (!containerRef.current) return { x: 50, y: 50 };
    const { width, height } = containerRef.current.getBoundingClientRect();
    // Оставляем отступы, чтобы мысли не появлялись за краями
    const x = Math.floor(Math.random() * (width - 150)) + 20;
    const y = Math.floor(Math.random() * (height - 60)) + 20;
    return { x, y };
  };

  // Спавн новых мыслей
  useEffect(() => {
    if (isGameOver) return;

    const spawnInterval = setInterval(() => {
      setThoughts((prev) => {
        // Ограничиваем количество активных мыслей (чтобы не засорять экран)
        const activeThoughts = prev.filter((t) => !t.isCaught);
        if (activeThoughts.length >= 6) return prev;

        const newThought = {
          id: Date.now() + Math.random(),
          text: triggers[Math.floor(Math.random() * triggers.length)],
          position: getRandomPosition(),
          isCaught: false,
        };

        return [...prev, newThought];
      });
    }, 1500);

    return () => clearInterval(spawnInterval);
  }, [isGameOver]);

  // Обработчик клика (поимка мысли)
  const catchThought = useCallback((id) => {
    setThoughts((prev) =>
      prev.map((thought) =>
        thought.id === id ? { ...thought, isCaught: true } : thought
      )
    );

    setScore((prevScore) => {
      const newScore = prevScore + 1;
      if (newScore >= 10) {
        setIsGameOver(true);
        // Очищаем оставшиеся мысли
        setThoughts((prev) => prev.map(t => ({ ...t, isCaught: true })));
      }
      return newScore;
    });

    // Удаляем мысль из массива после завершения анимации (500мс)
    setTimeout(() => {
      setThoughts((prev) => prev.filter((thought) => thought.id !== id));
    }, 500);
  }, []);

  // Рестарт игры
  const restartGame = () => {
    setScore(0);
    setThoughts([]);
    setIsGameOver(false);
  };

  return (
    <div
      ref={containerRef}
      className="relative w-full h-96 bg-sky-50 overflow-hidden rounded-3xl shadow-inner border border-sky-100"
    >
      {/* Счетчик */}
      <div className="absolute top-4 right-6 z-20 bg-white/80 backdrop-blur-sm px-4 py-1.5 rounded-full shadow-sm border border-sky-100">
        <span className="text-slate-600 font-medium text-sm">
          Поймано: {score} / 10
        </span>
      </div>

      {/* Отрисовка мыслей */}
      {!isGameOver &&
        thoughts.map((thought) => (
          <div
            key={thought.id}
            onClick={() => !thought.isCaught && catchThought(thought.id)}
            style={{
              left: `${thought.position.x}px`,
              top: `${thought.position.y}px`,
            }}
            className={`absolute cursor-pointer transition-all duration-500 ease-out select-none
              ${
                thought.isCaught
                  ? 'bg-emerald-100 text-emerald-700 scale-110 opacity-0'
                  : 'bg-white text-slate-600 shadow-md animate-pulse hover:shadow-lg hover:scale-105'
              }
              rounded-full px-4 py-2 font-medium text-sm z-10`}
          >
            {thought.isCaught ? 'Отпускаю...' : thought.text}
          </div>
        ))}

      {/* Победный экран */}
      {isGameOver && (
        <div className="absolute inset-0 flex flex-col items-center justify-center bg-sky-50/80 backdrop-blur-sm z-30 opacity-0 animate-[fadeIn_0.5s_ease-out_forwards]">
          <h3 className="font-serif text-2xl md:text-3xl text-slate-800 mb-4 text-center px-4">
            Выдыхайте.
          </h3>
          <p className="text-slate-600 text-center max-w-sm mb-8 px-4 font-light">
            Вы управляете своими мыслями, а не они вами.
          </p>
          <button
            onClick={restartGame}
            className="bg-deep-blue-900 text-white px-6 py-2.5 rounded-full hover:bg-blue-800 transition-colors shadow-sm font-medium"
          >
            Повторить
          </button>
        </div>
      )}

      {/* Tailwind keyframes для плавного появления победного экрана */}
      <style dangerouslySetInnerHTML={{ __html: `
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(10px); }
          to { opacity: 1; transform: translateY(0); }
        }
      `}} />
    </div>
  );
}
