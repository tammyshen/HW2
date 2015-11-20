import mediacloud, json, datetime

#replace if needed
def lookForKeyword(keyword):

    mc = mediacloud.api.MediaCloud('token')

    filter_set = [mc.publish_date_query(datetime.date(2015,8,1),datetime.date(2015,8,31)),'media_sets_id:1']
    numberCount = mc.sentenceCount(keyword,solr_filter=filter_set)
    return numberCount

#trump = lookForKeyword('Trump')
obama = lookForKeyword('Obama')


#print 'trump: '+str(trump['count'])
print 'obama: '+str(obama['count'])
