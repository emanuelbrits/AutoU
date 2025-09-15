import { useState } from "react";
import "./feedbackSection.css";

export default function FeedbackSection({ result }: { result: { categoria: string; mensagem: string } }) {
    const [feedback, setFeedback] = useState<"yes" | "no" | null>(null);
    const [suggestion, setSuggestion] = useState("");

    return (
        <div className="feedback-section">
            <h3>Essa resposta foi útil?</h3>
            <div className="buttons">
                <button
                    className={`feedback-btn ${feedback === "yes" ? "active" : ""}`}
                    onClick={() => {
                        setFeedback("yes");
                        setSuggestion("");
                    }}
                >
                    👍 Sim
                </button>
                <button
                    className={`feedback-btn ${feedback === "no" ? "active" : ""}`}
                    onClick={() => setFeedback("no")}
                >
                    👎 Não
                </button>
            </div>

            {feedback === "no" && (
                <div className="suggestion-box">
                    <textarea
                        placeholder="Digite a resposta que você sugeriria..."
                        value={suggestion}
                        onChange={(e) => setSuggestion(e.target.value)}
                        className="suggestion-input"
                    />
                </div>
            )}

            {feedback && (
                <p className="feedback-msg">
                    {feedback === "yes"
                        ? "Obrigado pelo feedback! ✅"
                        : "Obrigado! Sua sugestão pode ajudar a melhorar a resposta."}
                </p>
            )}
        </div>
    );
}
