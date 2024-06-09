import {
  Input,
  Button,
  Container,
  Text,
  Box,
  Flex,
  IconButton,
  Select
} from "@chakra-ui/react";
import Head from "next/head";
import { api } from "../config/api";
import { GetStaticProps } from "next";
import { IRankingModel } from "../models/document";
import Link from "next/link";

interface IDocumentPageProps {
  rankings: Array<IRankingModel>;
}

export default function DocumentPage({ rankings }: IDocumentPageProps) {
  async function onSubmit(event: React.FormEvent<HTMLFormElement>) {

    const response = await api.post("/ranking", {name: "Ranking 1"});

  }

  return (
    <>
      <Head>
        <title>Ranking | Saling Rankings</title>
      </Head>

      <Container p={4} maxW="container.md">
        <Flex mb={4} justifyContent="space-between" alignItems="center">
          <form onSubmit={onSubmit}>
            <Button colorScheme="teal" mt={4} type="submit">
              Novo Ranking
            </Button>
          </form>
          <Select placeholder="Selecione um ranking">
            <option value="1">Elo</option>
            <option value="2">Glicko</option>
            <option value="3">Glicko 2</option>
          </Select>
          <Select placeholder="Selecione um ano">
            <option value="2016">2016</option>
            <option value="2017">2017</option>
            <option value="2018">2018</option>
            <option value="2019">2019</option>
            <option value="2020">2020</option>
            <option value="2021">2021</option>
            <option value="2022">2022</option>
            <option value="2023">2023</option>
            <option value="2024">2024</option>
          </Select>         
        </Flex>

        <Flex direction="column" mb={4} alignItems="stretch">
          {rankings.map((ranking) => (
            
              <Box
                bg="gray.100"
                mb={2}
                px={6}
                py={4}
                borderRadius="md"
                w="full"
                _hover={{ bg: "gray.200" }}
                transition="background-color 100ms"
              >
                <Flex direction="column" alignItems="start" w="full">
                  <Text>{ranking.name}</Text>

                  <Text noOfLines={2} fontSize="sm" color="gray.500">
                    {ranking.score}
                  </Text>
                </Flex>
              </Box>
          ))}
        </Flex>
      </Container>
    </>
  );
}

export const getStaticProps: GetStaticProps = async (context) => {
  const response = await api.get("/ranking");
  const rankings = response.data as Record<string, number>[];
  const rankingsh = rankings.sort((a, b) => b.score - a.score);

    return {
      props: {
        rankings: rankingsh.map((ranking) => ({
          id: ranking.id,
          name: ranking.name,
          score: ranking.score,
          ano: ranking.ano,
          classe: ranking.classe,
        })),
      },
      revalidate: 1,
    };
};
