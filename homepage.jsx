import React from 'react';

const App = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-[#f8fff3] via-[#f4fce3] to-[#e1f3d8] p-6">

      <nav className="bg-[#c2c6aa] flex items-center justify-between px-4 py-3 shadow font-[Comfortaa]">
        <div className="flex items-center space-x-2">
          <button className="text-xl">☰</button>
          <div className="text-sm leading-tight">
            <div>therapy</div>
            <div>platform</div>
          </div>
        </div>
        <div className="hidden md:flex space-x-8 text-lg">
          <a href="#">Психологи</a>
          <a href="#">Чат</a>
          <a href="#">Профіль</a>
        </div>
      </nav>

      <main className="mt-12 px-4 md:px-16 lg:px-32">
        <h1 className="text-center text-4xl md:text-5xl font-[Anonymous_Pro] mb-10 leading-relaxed">
          Психологічна підтримка для тих, хто пройшов через війну
        </h1>

        <p className="text-xl leading-loose mb-10 font-sans max-w-3xl">
          Повернення з війни — це ще один бій, який часто не видно ззовні. Ми створили цю платформу, щоб ви могли знайти фахівця, який дійсно знає, що таке травма, тиша після бою, ніч без сну. Тут немає формальностей чи осуду — лише допомога. <br />
          Безпечно. Конфіденційно. Професійно.
        </p>

        <button className="bg-[#c2c6aa] text-black font-[Comfortaa] text-lg py-2 px-6 rounded-2xl shadow-md hover:bg-[#b0b39b]">
          Обрати психотерапевта
        </button>

        <div className="mt-40 text-right text-2xl md:text-3xl font-[Anonymous_Pro] leading-relaxed">
          <p>Ти не сам.</p>
          <p>Допомога поруч.</p>
        </div>
      </main>
    </div>
  );
};

export default App;
