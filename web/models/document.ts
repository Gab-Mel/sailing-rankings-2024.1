export interface IQuestionModel {
  id: number;
  text: string;
}
export interface IDocumentModel {
  id: number;
  title: string;
  content: string;
  questions?: IQuestionModel[];
}

export interface IRankingModel {
  id: number;
  name: string;
  ano: number;
  classe: string;
  score: number;
}

