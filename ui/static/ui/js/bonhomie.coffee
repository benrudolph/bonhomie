window.Bonhomie = {}

class Bonhomie.App

    DAY_INTERVAL: 7
    GITHUB_API: 'https://api.github.com'

    constructor: (options) ->
        @dayStart = 0
        @tags = options.tags

        @periods = ko.observableArray []

    loadEntries: ->
        $.get('/github/entries', {
            day_start: @dayStart
            day_end: @dayStart + @DAY_INTERVAL
        }).done (entries) =>
            @periods.push
                entries: entries
                dayStart: @dayStart
                dayEnd: @dayStart + @DAY_INTERVAL
            @dayStart += @DAY_INTERVAL

    getTagColor: (entry) ->
        TAG_NAME = 0
        TAG_COLOR = 1
        tag = _.find(@tags, (t) -> entry.tag == t[TAG_NAME])
        tag[TAG_COLOR]

    toggleEntryBody: (entry, e) =>
        e.preventDefault()
        $entryBody = $(e.currentTarget).find '~ .entry-body'
        $entryBody.toggleClass 'gone'

        unless entry.body?
            @getGithubMarkdown(entry).done (md) ->
                $entryBody.html md

    getGithubMarkdown: (entry) ->
        $.get("/github/markdown/#{entry.id}")

    displayPeriod: (period) ->
        start = moment().subtract(period.dayStart, 'days').format('LL')
        end = moment().subtract(period.dayEnd, 'days').format('LL')

        "#{start} - #{end}"

$(document).ready ->

    $('.tag-filter').click (e) ->
        $filter = $ @
        $filter.toggleClass 'tag-disabled'

        $entries = $ ".github-entry.#{$filter.data().tag}"

        if $filter.hasClass 'tag-disabled'
            $entries.addClass 'gone'
        else
            $entries.removeClass 'gone'

    $('.load-more').click (e) ->
        Bonhomie.app.loadEntries()
