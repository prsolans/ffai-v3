--
-- PostgreSQL database dump
--

-- Dumped from database version 11.3
-- Dumped by pg_dump version 11.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

DROP TABLE IF EXISTS fantasy_stats;
DROP TABLE IF EXISTS rankings;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS gamelog;
DROP SEQUENCE IF EXISTS fantasy_stats_stat_id_seq;
DROP SEQUENCE IF EXISTS rankings_id_seq;
DROP SEQUENCE IF EXISTS players_player_id_seq;
DROP SEQUENCE IF EXISTS teams_team_id_seq;

-- Name: fantasy_stats; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.fantasy_stats (
    stat_id integer NOT NULL,
    player_id integer,
    source text,
    year integer,
    points integer,
    url text
);


--
-- Name: fantasy_stats_stat_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.fantasy_stats_stat_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: fantasy_stats_stat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.fantasy_stats_stat_id_seq OWNED BY public.fantasy_stats.stat_id;



--
-- Name: rankings; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.rankings (
    id integer NOT NULL,
    source text,
    value integer,
    text text,
    player_id integer
);


--
-- Name: COLUMN rankings.value; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.rankings.value IS 'If there is a numeric metric';


--
-- Name: rankings_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.rankings_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: rankings_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.rankings_id_seq OWNED BY public.rankings.id;



--
-- Name: players; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.players (
    player_id integer NOT NULL,
    name text,
    age integer,
    experience integer,
    "position" text,
    team_id integer
);


--
-- Name: players_player_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.players_player_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: players_player_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.players_player_id_seq OWNED BY public.players.player_id;


--
-- Name: teams; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.teams (
    team_id integer NOT NULL,
    city text,
    name text,
    abbreviation text
);


--
-- Name: teams_team_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.teams_team_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: teams_team_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.teams_team_id_seq OWNED BY public.teams.team_id;


--
-- Name: fantasy_stats stat_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.fantasy_stats ALTER COLUMN stat_id SET DEFAULT nextval('public.fantasy_stats_stat_id_seq'::regclass);


--
-- Name: players player_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.players ALTER COLUMN player_id SET DEFAULT nextval('public.players_player_id_seq'::regclass);


--
-- Name: rankings id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rankings ALTER COLUMN id SET DEFAULT nextval('public.rankings_id_seq'::regclass);


--
-- Name: teams team_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.teams ALTER COLUMN team_id SET DEFAULT nextval('public.teams_team_id_seq'::regclass);


--
-- Name: fantasy_stats fantasy_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.fantasy_stats
    ADD CONSTRAINT fantasy_stats_pkey PRIMARY KEY (stat_id);


--
-- Name: players players_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.players
    ADD CONSTRAINT players_pkey PRIMARY KEY (player_id);


--
-- Name: rankings rankings_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rankings
    ADD CONSTRAINT rankings_pkey PRIMARY KEY (id);


--
-- Name: teams teams_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_pkey PRIMARY KEY (team_id);


--
-- Name: fantasy_stats fantasy_stats_player_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.fantasy_stats
    ADD CONSTRAINT fantasy_stats_player_id_fkey FOREIGN KEY (player_id) REFERENCES public.players(player_id);


--
-- Name: players players_team_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.players
    ADD CONSTRAINT players_team_id_fkey FOREIGN KEY (team_id) REFERENCES public.teams(team_id);


--
-- Name: rankings rankings_player_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rankings
    ADD CONSTRAINT rankings_player_id_fkey FOREIGN KEY (player_id) REFERENCES public.players(player_id);


--
-- PostgreSQL database dump complete
--

CREATE TABLE "public"."game_log" (
    "gamelog_id" serial,
    "player_id" integer,
    "game_location" text,
    "opponent" integer,
    "game_result" text,
    "pass_cmp" integer,
    "pass_att" integer,
    "pass_cmp_perc" numeric(3,2),
    "pass_yds" integer,
    "pass_td" integer,
    "pass_int" integer,
    "pass_rating" numeric(3,2),
    "pass_sacked" integer,
    "pass_sacked_yds" integer,
    "pass_yds_per_att" numeric(3,2),
    "pass_adj_yds_per_att" numeric(3,2),
    "rush_att" integer,
    "rush_yds" integer,
    "rush_yds_per_att" numeric(3,2),
    "rush_td" integer,
    "targets" integer,
    "rec" integer,
    "rec_yds" integer,
    "rec_yds_per_rec" numeric(3,2),
    "rec_td" integer,
    "catch_pct" numeric(3,2),
    "rec_yds_per_tgt" numeric(3,2),
    "all_td" integer,
    "scoring" integer,
    "fumbles" integer,
    "game_date" text,
    PRIMARY KEY ("gamelog_id"),
    FOREIGN KEY ("player_id") REFERENCES "public"."players"("player_id"),
    FOREIGN KEY ("opponent") REFERENCES "public"."teams"("team_id")
);
