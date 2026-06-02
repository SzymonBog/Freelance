from django.shortcuts import render, redirect
from .models import *
from random import randint
from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from .utils import get_plot
import pandas as pd
from dateutil.relativedelta import relativedelta


# Create your views here.
def generate_stocks_values():
    stocks_companies = StocksCompany.objects.all()

    if len(stocks_companies) == 0:
        names = ['Apex-Digital', 'Aurora-Mind', 'CloudPartners', 'Core-Cloud', 'Core-Flow', 'Core-Ocean', 'Core-Sky', 'CorePrime', 'CyberPartners', 'EarthCorp', 'EarthTechnologies', 'FlowSolutions', 'FlowStudio', 'FlowTechnologies', 'Flux-Tech', 'FluxFusion', 'FluxNexus', 'Fusion-Digital', 'FusionPrime', 'FusionSpectra', 'Lumina-Earth', 'Lumina-Tech', 'LuminaFlux', 'MindInc', 'MindTechnologies', 'Nexus-Solar', 'NexusPrime', 'NovaZenith', 'PeakVentures', 'Pioneer-Sky', 'Prime-Digital', 'Prime-Earth', 'PrimePioneer', 'PrimeQuantum', 'Pulse-Flow', 'Pulse-Star', 'PulseAurora', 'PulseNova', 'Quantum-Mind', 'QuantumVista', 'SkyInnovations', 'SkyPartners', 'SolarInc', 'SolarStudio', 'SolarTechnologies', 'SparkStudio', 'Spectra-Cyber', 'Spectra-Earth', 'SpectraVista', 'VistaQuantum']
        dates = []
        date = pd.date_range(start='2025-01-01', end='2028-12-31', freq='D')

        for i in range(50):
            dates.append(date)

        prices = []

        """
        chance_1_3_pct = 28  # 28
        chance_4_10_pct = 70  # 42
        chance_10_20_pct = 100  # 30
        """

        # print(len(dates[0]))  # 730

        for i in range(50):
            stock_prices = []
            for j in range(len(dates[0])):
                if j == 0:
                    tier = randint(1, 3)
                    price = 500

                    if tier == 1:
                        price = randint(50, 80)
                    elif tier == 2:
                        price = randint(120, 180)
                    else:
                        price = randint(200, 4000)

                    stock_prices.append(price)

                else:
                    if 10 < stock_prices[j-1] < 10000:
                        minus = randint(0, 1)

                        if minus > 0:

                            chance = randint(1, 100)

                            if chance <= 50:
                                pct = randint(0, 3)
                            elif 50 < chance <= 90:
                                pct = randint(4, 10)
                            else:
                                pct = randint(10, 20)

                        else:

                            chance = randint(1, 100)

                            if chance <= 50:
                                pct = randint(-3, 0)
                            elif 50 < chance <= 90:
                                pct = randint(-10, -4)
                            else:
                                pct = randint(-20, -10)
                    else:

                        if stock_prices[j-1] < 10:
                            pct = randint(200, 1000)

                        elif stock_prices[j-1] > 10000:
                            pct = randint(-90, -60)

                    stock_prices.append(round(stock_prices[j-1] * (1 + (pct / 100)), 2))

            prices.append(stock_prices)

        for i in range(50):
            for j in range(len(dates[0])):
                StocksCompany.objects.create(
                    companyName=names[i],
                    date=dates[i][j],
                    sharePrice=prices[i][j]
                )

        print(prices)

        print("Generated stocks")
    else:
        print("Stocks have already been generated")


def index(request):
    generate_stocks_values()
    """
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
    x_ticks = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    chart = get_plot(x, y, title="test", width=10, inside_color="black", outside_color="gray", x_ticks=x_ticks)
    """
    company1 = StocksCompany.objects.filter(companyName='PulseAurora')  # (companyName="FlowTechnologies")

    # only last 3 months
    months_earlier = None

    if months_earlier is not None:
        now = datetime.now().date()
        earlier_date = now - relativedelta(months=months_earlier)
        to_stay = []

        for i in company1:
            if earlier_date <= i.date <= now:
                to_stay.append(i)

        company1 = to_stay
    #

    x = [x.date for x in company1]
    y = [y.sharePrice for y in company1]

    color = 'green'
    colors = ['green']

    for i in range(len(company1)):
        if i != 0:
            if company1[i].sharePrice >= company1[i-1].sharePrice:
                colors.append('green')
            else:
                colors.append('red')

    company = company1[0]
    chart = get_plot(x, y, title=company.companyName, outside_color='gray', inside_color='darkgrey', color=color, bar_plot_colors=colors)
    return render(request, 'plot.html', {
        'plot': chart
    })
