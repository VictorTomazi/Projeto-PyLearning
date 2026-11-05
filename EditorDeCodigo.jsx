import CodeMirror from '@uiw/react-codemirror';
import { python } from '@codemirror/lang-python';
import { indentUnit } from '@codemirror/language';

// Definidas fora do componente para manter a mesma referência entre renders.
const EXTENSOES = [
  python(),              // Realce de sintaxe e indentação automática para Python
  indentUnit.of('    '), // Tab/indentação com 4 espaços (padrão PEP 8)
];

export default function EditorDeCodigo({ value, onChange }) {
  return (
    <CodeMirror
      value={value}
      onChange={(novoCodigo) => onChange(novoCodigo)}
      extensions={EXTENSOES}
      theme="dark"
      height="300px"
    />
  );
}
