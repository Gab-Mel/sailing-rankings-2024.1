import Head from "next/head";
import {
  FormControl,
  FormLabel,
  Input,
  Textarea,
  FormHelperText,
  Button,
  Container,
} from "@chakra-ui/react";
import { api } from "../../config/api";
import { useRouter } from "next/router";

export default function NewRankingPage() {
  const router = useRouter();

  
  async function onSubmit() {

    await api.post("/ranking");

    /*
    if (response.status === 201) {
      console.log(response.data);
      const document = response.data;
      router.push(`/documents/${document.id}`);
    }
    */
  }

  return (
    <>
      <Head>
        <title>Novo texto | Cats are liquid!</title>
      </Head>

      <Container p={4} maxW="container.md">
        <form onSubmit={onSubmit}>
          <Button mt={4} colorScheme="teal" type="submit">
            Salvar
          </Button>
        </form>
      </Container>
    </>
  );
}
