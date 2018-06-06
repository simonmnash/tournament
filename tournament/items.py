# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TournamentItem(scrapy.Item):
    pass

class DeckListItem(TournamentItem):
    mtgtop8_deck_id = scrapy.Field()
    mtgtop8_event_id = scrapy.Field()
    pilot = scrapy.Field()
    placing = scrapy.Field()
    deck_name = scrapy.Field()
    decklist_url = scrapy.Field()
