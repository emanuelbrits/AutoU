import { BiText } from 'react-icons/bi'
import './App.css'
import { FaFile } from 'react-icons/fa'
import { useState } from 'react'
import { IoSend } from 'react-icons/io5'
import { FaFileArrowUp } from 'react-icons/fa6'

function App() {
  const [isText, setIsText] = useState(true)
  const [result, setResult] = useState<{ categoria: string; mensagem: string } | null>(null)
  const [emailText, setEmailText] = useState("")
  const [dragActive, setDragActive] = useState(false);
  const [file, setFile] = useState<File | null>(null);

  const handleFile = (f: File) => {
    setFile(f);
    setResult({ categoria: "Produtivo", mensagem: `Arquivo "${f.name}" enviado com sucesso!` });
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      handleFile(e.target.files[0]);
    }
  };

  const handleDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFile(e.dataTransfer.files[0]);
    }
  };

  const handleDrag = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  };

  return (
    <>
      <div className='App'>
        <div className='switch-buttons'>
          <button className={isText ? 'active' : ''} onClick={() => { setIsText(true); setResult(null); }}><BiText /> Texto</button>
          <button className={!isText ? 'active' : ''} onClick={() => { setIsText(false); setResult(null); }}><FaFile /> Arquivo</button>
        </div>
        {isText ? (
          <div className='text-section'>
            <div className='email-form'>
              <textarea placeholder="Digite o texto do email" className='email-input' value={emailText} onChange={(e) => setEmailText(e.target.value)} />
              <button type="submit" className='submit-button' onClick={() => setEmailText(emailText)}><IoSend /></button>
            </div>
            <div className='result'>
              <h2>Resultado</h2>
              {result ? (
                <div className='result-content'>
                  <p>Categoria: {result.categoria}</p>
                  <p>Mensagem sugerida: {result.mensagem}</p>
                </div>
              ) : (
                <p className='no-result'>Envie um email para checar a categoria e resposta sugerida</p>
              )}
            </div>
          </div>
        ) : (
          <div className="file-section">
            <div
              className={`file-form ${dragActive ? "drag-active" : ""}`}
              onDragEnter={handleDrag}
              onDragOver={handleDrag}
              onDragLeave={handleDrag}
              onDrop={handleDrop}
            >
              <div className="drop-area">
                <input
                  type="file"
                  id="file-upload"
                  className="file-input"
                  onChange={handleChange}
                  hidden
                />
                <FaFileArrowUp size={48} />
                {!file ? (
                  <label htmlFor="file-upload" className="file-label">
                    Arraste o arquivo <br />
                    <span className="file-hint">ou clique aqui</span>
                  </label>
                ) : (
                  <div className="file-selected">
                    <span>{file.name}</span>
                    <button
                      type="button"
                      className="remove-button"
                      onClick={() => setFile(null)}
                    >
                      Limpar
                    </button>
                  </div>
                )}
              </div>
            </div>

            <div className="result">
              <h2>Resultado</h2>
              {result ? (
                <div className="result-content">
                  <p>Categoria: {result.categoria}</p>
                  <p>Mensagem sugerida: {result.mensagem}</p>
                </div>
              ) : (
                <p className="no-result">
                  Adicione um arquivo para checar a categoria e resposta sugerida
                </p>
              )}
            </div>
          </div>
        )}
      </div>
    </>
  )
}

export default App
