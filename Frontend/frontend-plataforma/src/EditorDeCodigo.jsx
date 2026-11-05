import CodeMirror from '@uiw/react-codemirror';
// 1. Importe a extensão do Python
import { python } from '@codemirror/lang-python';

export default function EditorDeCodigo({ value, onChange }) {
  return (
    <div style={{ border: '2px solid #ccc', borderRadius: '8px', overflow: 'hidden' }}>
      <CodeMirror
        value={value}
        onChange={onChange}
        height="200px"
        theme="dark" // Deixa o fundo escuro, com cara de terminal
        // 2. Ative a extensão aqui:
        extensions={[python()]} 
      />
    </div>
  );
}