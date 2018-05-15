# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from tournament.items import DeckListItem


class Mtgtop8Spider(scrapy.Spider):
    name = 'mtgtop8'
    allowed_domains = ['http://mtgtop8.com/']
    start_urls = ['http://mtgtop8.com/event?e=1']

    def parse(self, response):
        page = response.url.split("/")[-2]
        # Get the name, pilot, and placing of the current decklist.
        # This selector returns an array of the form ['\n\t\t\t', PLACING, '\n\t\t\t', NAME, '\n\t\t\t', PILOT]
        placing_name_pilot = Selector(response).xpath("//div[contains(@class, 'chosen_tr')]//text()").extract()
        placing = placing_name_pilot[1]
        deck_name = placing_name_pilot[3]
        pilot = placing_name_pilot[5]
        # Get the decklist as a txt file.
        decklist_link = Selector(response).xpath("//a[contains(text(),'MTGO')]").extract()
        # Get the links to other decks in this tornament.
        other_decklists = Selector(response).xpath( "//div[contains(@class, 'hover_tr')]//div[contains(@class, 'S14')]//a//@href").extract()
        # Grab the format and date from the heading of the leaderboard
        format_date = Selector(response).xpath("//td[contains(@class, 'S14')]/text()").extract()
        format = format_date[0]
        date = format_date[1]
        #print(str([placing, name, pilot, format, date]))

        item = DeckListItem()
        item["placing"] = placing
        item["deck_name"] = deck_name
        item["pilot"] = pilot
        item["decklist_url"] = decklist_link
        yield item
        pass
