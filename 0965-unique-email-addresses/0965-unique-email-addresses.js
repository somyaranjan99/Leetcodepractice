/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    let emailSet=new Set()
    for(let email of emails){
        let emailDomain= email.split('@')
        let name=emailDomain[0]
        let domain= emailDomain[1]
        name=name.split('+')[0]
        name=name.replaceAll('.','')
        let unique=name+'@'+domain
        emailSet.add(unique)

    }
    return emailSet.size
};