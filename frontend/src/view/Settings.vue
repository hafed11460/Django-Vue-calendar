<template>
  <div class="container">
    <small><a href="javascript:void(0)">Settings</a></small>
    <br />
    <b-tabs small horizontal>
      <b-tab title="Company details">
        <b-card>
          <b-row>
            <b-col cols="12">
              <h4>User Settings</h4>
            </b-col>
            <b-col cols="12">
              <div class="GFS-Center-Table">
                <b-button
                  variant="warning"
                  to="/edit-companydetails"
                  style="float: right; padding: 8px 24px"
                  >Edit</b-button
                >
                <table class="table table-hover">
                  <tbody>
                    <tr>
                      <td>Company name</td>
                      <td>{{ company.company || "No Name" }}</td>
                      <td></td>
                    </tr>
                    <tr>
                      <td>Website</td>
                      <td>{{ company.website || "No Website" }}</td>
                      <td></td>
                    </tr>
                    <tr>
                      <td>Address</td>
                      <td>{{ company.address || "No Address" }}</td>
                      <td></td>
                    </tr>
                    <tr>
                      <td>Contact numbers</td>
                      <td>{{ company.contactNumber || "No Contact" }}</td>
                      <td></td>
                    </tr>
                    <tr>
                      <td>Logo</td>
                      <td v-if="company.logo">
                        <img :src="company.logo" alt="company-logo" style="max-height: 60px" />
                      </td>
                      <td v-else>No Logo</td>
                      <td></td>
                    </tr>
                    <tr>
                      <td>Company ID</td>
                      <td>{{ company.user }}</td>
                      <td>Account's unique ID</td>
                    </tr>
                    <tr>
                      <td>Genuine Data</td>
                      <td>
                        <span v-if="genuine">
                          <svg
                            width="19"
                            height="15"
                            viewBox="0 0 17 13"
                            version="1.1"
                            xmlns="http://www.w3.org/2000/svg"
                            xmlns:xlink="http://www.w3.org/1999/xlink"
                          >
                            <path
                              d="M5.81105 12.59L0 6.7792L1.93685 4.84235L5.81105 8.7163L14.5271 0L16.464 1.93685L5.81105 12.59Z"
                              fill="#1DC724"
                            ></path>
                          </svg>
                        </span>
                        <span v-else
                          >Not verified,
                          <a href="mailto:admin@hotelfacts.net">Contact admin</a></span
                        >
                      </td>
                      <td>Data verified by Ananas App moderators</td>
                    </tr>
                    <tr>
                      <td>Premium Account</td>
                      <td>
                        <span v-if="premium">
                          <svg
                            width="80"
                            height="30"
                            viewBox="0 0 80 22"
                            fill="none"
                            xmlns="http://www.w3.org/2000/svg"
                          >
                            <rect width="80" height="22" rx="5" fill="#1DC724"></rect>
                            <text
                              font-weight="bold"
                              letter-spacing="2px"
                              xml:space="preserve"
                              text-anchor="start"
                              font-family="Noto Sans JP"
                              font-size="12"
                              id="svg_6"
                              y="15"
                              x="4"
                              stroke-width="0"
                              stroke="#000"
                              fill="#ffffff"
                            >
                              PREMIUM
                            </text>
                          </svg></span
                        ><span v-else><b-link to="/premium-account">Upgrade Here</b-link></span>
                      </td>
                      <td>Unlock features and exclusive access</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </b-col>
          </b-row>
        </b-card>
      </b-tab>
      <b-tab title="Preferences">
        <b-card>
          <b-row>
            <b-col cols="12">
              <h4>Preference settings</h4>
            </b-col>
            <b-col cols="12">
              <div class="GFS-Center-Table">
                <b-button
                  variant="warning"
                  to="/edit-preference"
                  style="float: right; padding: 8px 24px"
                  >Edit</b-button
                >
                <table class="table table-hover">
                  <tbody>
                    <tr>
                      <td>Audit trail</td>
                      <td>{{ convertBool(preferences.auditTrail) }}</td>
                      <td></td>
                    </tr>
                    <tr>
                      <td>Add Company Logo on docs</td>
                      <td>{{ convertBool(preferences.addLogo) }}</td>
                      <td></td>
                    </tr>
                    <tr>
                      <td>Partners overriding fact documents</td>
                      <td>
                        {{ convertBool(preferences.partnerOverrideFacts) }}
                      </td>
                      <td></td>
                    </tr>
                    <tr>
                      <td>overriding moderation</td>
                      <td>
                        {{ moderate }}
                        <b-icon
                          icon="question-circle-fill"
                          scale="1.2"
                          variant="primary"
                          aria-label="Help"
                        ></b-icon>
                      </td>
                      <td></td>
                    </tr>
                    <!--                     <tr>
                      <td>App Theme colors</td>
                      <td>Change interface color preference</td>
                      <td>
                        <b-button @click="changeTheme()">Change</b-button>
                      </td>
                      <transition name="slide" appear>
                        <div
                          class="modal"
                          v-if="themeChanger"
                          style="text-align: left; display: block; width: 100%; float: left"
                        >
                          <fixed-plugin :color.sync="themeColor"> </fixed-plugin>
                          <b-button variant="success" @click="saveTheme()" style="float: right"
                            >confirm</b-button
                          >
                        </div>
                      </transition>
                    </tr> -->
                  </tbody>
                </table>
              </div>
            </b-col>
          </b-row>
        </b-card>
      </b-tab>
      <b-tab v-if="accountType === 'accommodation'" title="Layout">
        <b-card>
          <b-row>
            <b-col cols="12">
              <h4>Layout settings</h4>
            </b-col>
            <b-col cols="12">
              <div class="GFS-Center-Table">
                <b-button
                  variant="warning"
                  to="/edit-layoutsettings"
                  style="float: right; padding: 8px 24px"
                  >Edit</b-button
                >
                <table class="table table-hover">
                  <tbody>
                    <tr>
                      <td>Export PDF layout</td>
                      <td>{{ layout(preferences.pdfLayout) }}</td>
                      <td></td>
                    </tr>
                    <tr>
                      <td>Website API layout</td>
                      <td>{{ layout(preferences.apiLayout) }}</td>
                      <td></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </b-col>
          </b-row>
        </b-card>
      </b-tab>
      <b-tab title="Security">
        <b-card>
          <b-row>
            <b-col cols="12">
              <h4>Security settings</h4>
            </b-col>
            <b-col cols="12">
              <div class="GFS-Center-Table">
                <b-button
                  variant="warning"
                  to="/edit-securitysettings"
                  style="float: right; padding: 8px 24px"
                  >Edit</b-button
                >
                <table class="table table-hover">
                  <tbody>
                    <tr>
                      <td>Password</td>
                      <td>Last change: xx-xx-xxxx</td>
                      <td></td>
                    </tr>
                    <tr>
                      <td>
                        Email <br />
                        {{ userInfo }}
                      </td>
                      <td>Status : Verified / Not</td>
                      <td></td>
                    </tr>
                    <tr>
                      <td>Two-factor authentication</td>
                      <td>Coming soon</td>
                      <td></td>
                    </tr>
                    <tr>
                      <td>Audit Log</td>
                      <td><a href="/audit-trail">Review</a></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </b-col>
          </b-row>
        </b-card>
        <span style="font-style: italic; display: inline-block; margin: 3px 0"
          >Changing your e-mail address will log you out and require you to verify the new e-mail
          address.</span
        >
      </b-tab>
      <b-tab title="Mailing">
        <b-card>
          <b-row>
            <b-col cols="12">
              <h4>Email settings</h4>
            </b-col>
            <b-col cols="12">
              <div class="GFS-Center-Table">
                <b-button
                  variant="warning"
                  to="/edit-mailingdetails"
                  style="float: right; padding: 8px 24px"
                  >Edit</b-button
                >
                <table class="table table-hover">
                  <tbody>
                    <tr>
                      <td>Email addresses</td>
                      <td>{{ preferences.emailAddresses }}</td>
                      <td></td>
                    </tr>
                    <tr>
                      <td>Partnership:</td>
                      <td>{{ mail(preferences.partnershipNewMail) }}Send mail on new</td>
                      <td>{{ mail(preferences.partnershipChangesMail) }}Send mail on changes</td>
                    </tr>
                    <tr>
                      <td>New features & offers</td>
                      <td>{{ mail(preferences.featuresOffersMail) }}Notify via mails</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </b-col>
          </b-row>
        </b-card>
      </b-tab>
      <b-tab title="Notifications">
        <b-card>
          <b-row>
            <b-col cols="12">
              <h4>Notification settings</h4>
            </b-col>
            <b-col cols="12">
              <div class="GFS-Center-Table">
                <b-button
                  variant="warning"
                  to="/edit-notifications"
                  style="float: right; padding: 8px 24px"
                  >Edit</b-button
                >
                <table class="table table-hover">
                  <tbody>
                    <tr>
                      <td>Partnership request</td>
                      <td>
                        {{ convertBool(preferences.notifyPartnershipRequest) }}
                      </td>
                    </tr>
                    <tr>
                      <td>Partnership changes</td>
                      <td>
                        {{ convertBool(preferences.notifyPartnershipChanges) }}
                      </td>
                    </tr>
                    <tr>
                      <td>Factsheet updated</td>
                      <td>
                        {{ convertBool(preferences.notifyFactSheetChanges) }}
                      </td>
                    </tr>
                    <tr>
                      <td>Partner downloaded fact doc</td>
                      <td>
                        {{ convertBool(preferences.notifyFactSheetDownload) }}
                      </td>
                    </tr>
                    <tr>
                      <td>Partner requesting fact review</td>
                      <td>{{ convertBool(preferences.notifyFactReview) }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </b-col>
          </b-row>
        </b-card>
      </b-tab>
      <b-tab title="Payment & Billing">
        <b-card>
          <b-row>
            <div class="dlKcPR bsTCOW">
              <h4 size="16">You are using the Ananas {{ planText }} plan</h4>
              <p>
                Track your offline bookings, integrate with Viator to manage availability and
                bookings and get additional distributions through the Affiliate hub.
              </p>
              <div v-if="preferences.plan === 'F'" class="sc-ehCJOs jNbSbr">
                <b-button variant="success" to="/subscribe">Upgrade to PREMIUM</b-button>
              </div>
            </div>
          </b-row>
          <b-row>
            <b-col cols="12">
              <h4>Payment and Billing</h4>
            </b-col>
          </b-row>
          <b-row>
            <b-col cols="12">
              <b-tabs>
                <b-tab title="Account overview">
                  <div class="container" style="margin: 30px 0px">
                    <b-row>
                      <b-col cols="5">
                        <b-row>
                          <b-col>
                            <b-card style="border-radius: 15px">
                              <div>
                                <h4 size="15">Payment details</h4>
                                <p>No payment method registered.</p>
                                <svg
                                  width="80"
                                  height="54"
                                  viewBox="0 0 80 54"
                                  fill="none"
                                  xmlns="http://www.w3.org/2000/svg"
                                  style="opacity: 0.5"
                                >
                                  <rect width="80" height="54" rx="6" fill="#1D57C7"></rect>
                                  <path
                                    fill-rule="evenodd"
                                    clip-rule="evenodd"
                                    d="M9 10.5C9 9.67157 9.67157 9 10.5 9H31.5C32.3284 9 33 9.67157 33 10.5C33 11.3284 32.3284 12 31.5 12H10.5C9.67157 12 9 11.3284 9 10.5Z"
                                    fill="white"
                                  ></path>
                                  <path
                                    fill-rule="evenodd"
                                    clip-rule="evenodd"
                                    d="M9 44.5C9 43.6716 9.65558 43 10.4643 43H48.5357C49.3444 43 50 43.6716 50 44.5C50 45.3284 49.3444 46 48.5357 46H10.4643C9.65558 46 9 45.3284 9 44.5Z"
                                    fill="white"
                                  ></path>
                                  <path
                                    d="M10.6528 35.9465H9.89937V32.9679L9 33.254V32.6257L10.572 32.0481H10.6528V35.9465Z"
                                    fill="white"
                                  ></path>
                                  <path
                                    d="M14.4901 35.9465H11.8884V35.4171L13.1163 34.0749C13.2848 33.8859 13.4091 33.721 13.4891 33.5802C13.5707 33.4394 13.6116 33.3057 13.6116 33.1791C13.6116 33.0062 13.569 32.8708 13.4838 32.7727C13.3987 32.6729 13.277 32.623 13.1189 32.623C12.9486 32.623 12.8139 32.6836 12.7148 32.8048C12.6175 32.9242 12.5688 33.082 12.5688 33.2781H11.8128C11.8128 33.041 11.8676 32.8244 11.9771 32.6283C12.0883 32.4323 12.2447 32.279 12.4463 32.1684C12.6479 32.0561 12.8764 32 13.1319 32C13.5229 32 13.8262 32.0963 14.0417 32.2888C14.259 32.4813 14.3676 32.7531 14.3676 33.1043C14.3676 33.2968 14.3189 33.4929 14.2216 33.6925C14.1243 33.8922 13.9574 34.1248 13.7211 34.3904L12.8582 35.3235H14.4901V35.9465Z"
                                    fill="white"
                                  ></path>
                                  <path
                                    d="M15.7205 33.6578H16.122C16.3132 33.6578 16.4548 33.6087 16.5469 33.5107C16.639 33.4127 16.6851 33.2825 16.6851 33.1203C16.6851 32.9635 16.639 32.8414 16.5469 32.754C16.4566 32.6667 16.3314 32.623 16.1715 32.623C16.0273 32.623 15.9065 32.664 15.8092 32.746C15.7119 32.8262 15.6632 32.9314 15.6632 33.0615H14.9098C14.9098 32.8583 14.9628 32.6765 15.0688 32.516C15.1766 32.3538 15.326 32.2273 15.5172 32.1364C15.7101 32.0455 15.9221 32 16.1533 32C16.5547 32 16.8693 32.0989 17.097 32.2968C17.3246 32.4929 17.4385 32.7638 17.4385 33.1096C17.4385 33.2879 17.3855 33.4519 17.2795 33.6016C17.1734 33.7513 17.0344 33.8663 16.8624 33.9465C17.0761 34.025 17.2351 34.1426 17.3394 34.2995C17.4454 34.4563 17.4984 34.6417 17.4984 34.8556C17.4984 35.2014 17.375 35.4786 17.1283 35.6872C16.8832 35.8957 16.5582 36 16.1533 36C15.7744 36 15.4642 35.8975 15.2226 35.6925C14.9828 35.4875 14.8629 35.2166 14.8629 34.8797H15.6163C15.6163 35.0258 15.6693 35.1453 15.7753 35.238C15.883 35.3307 16.0151 35.377 16.1715 35.377C16.3505 35.377 16.4904 35.3289 16.5912 35.2326C16.6938 35.1346 16.745 35.0053 16.745 34.8449C16.745 34.4563 16.5365 34.262 16.1194 34.262H15.7205V33.6578Z"
                                    fill="white"
                                  ></path>
                                  <path
                                    d="M20.2487 34.4813H20.6788V35.1043H20.2487V35.9465H19.4953V35.1043H17.939L17.9051 34.6176L19.4875 32.0535H20.2487V34.4813ZM18.6559 34.4813H19.4953V33.107L19.4458 33.1952L18.6559 34.4813Z"
                                    fill="white"
                                  ></path>
                                  <path
                                    d="M23.8566 34.0321L24.0756 32.0535H26.2028V32.6979H24.6934L24.5996 33.5348C24.7786 33.4367 24.9689 33.3877 25.1705 33.3877C25.532 33.3877 25.8153 33.5027 26.0203 33.7326C26.2254 33.9626 26.3279 34.2843 26.3279 34.6979C26.3279 34.9492 26.2758 35.1747 26.1715 35.3743C26.069 35.5722 25.9213 35.7264 25.7284 35.8369C25.5355 35.9456 25.3078 36 25.0454 36C24.816 36 24.6031 35.9528 24.4067 35.8583C24.2103 35.762 24.0547 35.6275 23.94 35.4545C23.8271 35.2816 23.7671 35.0847 23.7602 34.8636H24.5057C24.5214 35.0258 24.5761 35.1524 24.67 35.2433C24.7656 35.3324 24.8898 35.377 25.0428 35.377C25.2131 35.377 25.3443 35.3146 25.4364 35.1898C25.5285 35.0633 25.5746 34.885 25.5746 34.6551C25.5746 34.434 25.5216 34.2647 25.4155 34.1471C25.3095 34.0294 25.1592 33.9706 24.9645 33.9706C24.7855 33.9706 24.6404 34.0187 24.5292 34.115L24.4562 34.1845L23.8566 34.0321Z"
                                    fill="white"
                                  ></path>
                                  <path
                                    d="M28.854 32.0134V32.6497H28.781C28.4404 32.6551 28.1658 32.746 27.9572 32.9225C27.7504 33.0989 27.6262 33.344 27.5845 33.6578C27.7861 33.4474 28.0407 33.3422 28.3483 33.3422C28.6785 33.3422 28.9409 33.4635 29.1356 33.7059C29.3302 33.9483 29.4275 34.2674 29.4275 34.6631C29.4275 34.9162 29.3737 35.1453 29.2659 35.3503C29.1599 35.5553 29.0087 35.7148 28.8123 35.8289C28.6177 35.943 28.3969 36 28.1502 36C27.7504 36 27.4272 35.8574 27.1804 35.5722C26.9354 35.287 26.8128 34.9064 26.8128 34.4305V34.1524C26.8128 33.7299 26.8902 33.3574 27.0448 33.0348C27.2013 32.7103 27.4246 32.4599 27.7148 32.2834C28.0068 32.1052 28.3448 32.0152 28.7289 32.0134H28.854ZM28.1189 33.9626C27.9972 33.9626 27.8869 33.9955 27.7878 34.0615C27.6887 34.1257 27.6157 34.2112 27.5688 34.3182V34.5535C27.5688 34.8119 27.6184 35.0143 27.7174 35.1604C27.8165 35.3048 27.9555 35.377 28.1345 35.377C28.2961 35.377 28.4265 35.3119 28.5255 35.1818C28.6263 35.0499 28.6767 34.8797 28.6767 34.6711C28.6767 34.459 28.6263 34.2879 28.5255 34.1578C28.4247 34.0276 28.2892 33.9626 28.1189 33.9626Z"
                                    fill="white"
                                  ></path>
                                  <path
                                    d="M32.4567 32.4866L30.9891 35.9465H30.194L31.6642 32.6791H29.7769V32.0535H32.4567V32.4866Z"
                                    fill="white"
                                  ></path>
                                  <path
                                    d="M35.4155 33.0882C35.4155 33.2772 35.3695 33.4447 35.2774 33.5909C35.1853 33.7371 35.0584 33.8538 34.8968 33.9412C35.081 34.0321 35.227 34.1578 35.3347 34.3182C35.4425 34.4768 35.4964 34.664 35.4964 34.8797C35.4964 35.2255 35.3816 35.4991 35.1522 35.7005C34.9228 35.9002 34.6109 36 34.2164 36C33.8219 36 33.509 35.8993 33.2779 35.6979C33.0468 35.4964 32.9312 35.2237 32.9312 34.8797C32.9312 34.664 32.9851 34.4759 33.0928 34.3155C33.2006 34.1551 33.3457 34.0303 33.5282 33.9412C33.3665 33.8538 33.2397 33.7371 33.1476 33.5909C33.0572 33.4447 33.012 33.2772 33.012 33.0882C33.012 32.7567 33.1197 32.4929 33.3352 32.2968C33.5507 32.0989 33.8436 32 34.2138 32C34.5822 32 34.8742 32.098 35.0897 32.2941C35.3069 32.4884 35.4155 32.7531 35.4155 33.0882ZM34.7404 34.8235C34.7404 34.6542 34.6926 34.5187 34.597 34.4171C34.5014 34.3155 34.3728 34.2647 34.2112 34.2647C34.0513 34.2647 33.9235 34.3155 33.8279 34.4171C33.7324 34.5169 33.6846 34.6524 33.6846 34.8235C33.6846 34.9893 33.7315 35.123 33.8253 35.2246C33.9192 35.3262 34.0495 35.377 34.2164 35.377C34.3797 35.377 34.5075 35.328 34.5996 35.2299C34.6934 35.1319 34.7404 34.9964 34.7404 34.8235ZM34.6621 33.1257C34.6621 32.9742 34.623 32.8529 34.5448 32.762C34.4666 32.6693 34.3563 32.623 34.2138 32.623C34.073 32.623 33.9635 32.6676 33.8853 32.7567C33.8071 32.8458 33.768 32.9688 33.768 33.1257C33.768 33.2807 33.8071 33.4055 33.8853 33.5C33.9635 33.5945 34.0739 33.6417 34.2164 33.6417C34.3589 33.6417 34.4684 33.5945 34.5448 33.5C34.623 33.4055 34.6621 33.2807 34.6621 33.1257Z"
                                    fill="white"
                                  ></path>
                                  <path
                                    d="M40.4286 34.3904C40.2322 34.5882 40.0028 34.6872 39.7404 34.6872C39.4049 34.6872 39.1364 34.5695 38.9348 34.3342C38.7332 34.0971 38.6324 33.7781 38.6324 33.377C38.6324 33.1221 38.6863 32.8886 38.7941 32.6765C38.9035 32.4626 39.0556 32.2968 39.2503 32.1791C39.4449 32.0597 39.6639 32 39.9072 32C40.1575 32 40.3799 32.0642 40.5746 32.1925C40.7692 32.3209 40.9204 32.5053 41.0282 32.746C41.1359 32.9866 41.1907 33.262 41.1924 33.5722V33.8583C41.1924 34.5071 41.0351 35.0169 40.7205 35.3877C40.406 35.7585 39.9602 35.9563 39.3832 35.9813L39.1981 35.984V35.3396L39.365 35.3369C40.0202 35.3066 40.3747 34.9911 40.4286 34.3904ZM39.9254 34.0963C40.0471 34.0963 40.1514 34.0642 40.2383 34C40.3269 33.9358 40.3938 33.8583 40.439 33.7674V33.4492C40.439 33.1872 40.3903 32.984 40.293 32.8396C40.1957 32.6952 40.0653 32.623 39.902 32.623C39.7508 32.623 39.6265 32.6943 39.5292 32.8369C39.4319 32.9777 39.3832 33.1551 39.3832 33.369C39.3832 33.5811 39.4301 33.7558 39.524 33.893C39.6196 34.0285 39.7534 34.0963 39.9254 34.0963Z"
                                    fill="white"
                                  ></path>
                                  <path
                                    d="M43.562 35.9465H42.8087V32.9679L41.9093 33.254V32.6257L43.4812 32.0481H43.562V35.9465Z"
                                    fill="white"
                                  ></path>
                                  <path
                                    d="M47.3525 34.3369C47.3525 34.8752 47.2438 35.287 47.0266 35.5722C46.8094 35.8574 46.4913 36 46.0725 36C45.6588 36 45.3425 35.8601 45.1236 35.5802C44.9046 35.3004 44.7925 34.8993 44.7873 34.377V33.6604C44.7873 33.1168 44.8968 32.7041 45.1157 32.4225C45.3365 32.1408 45.6536 32 46.0673 32C46.4809 32 46.7972 32.1399 47.0162 32.4198C47.2351 32.6979 47.3472 33.098 47.3525 33.6203V34.3369ZM46.5991 33.5508C46.5991 33.2282 46.5556 32.9938 46.4687 32.8476C46.3836 32.6996 46.2497 32.6257 46.0673 32.6257C45.89 32.6257 45.7588 32.6961 45.6736 32.8369C45.5902 32.9759 45.5459 33.1943 45.5407 33.492V34.4385C45.5407 34.7558 45.5824 34.992 45.6658 35.1471C45.751 35.3004 45.8865 35.377 46.0725 35.377C46.2567 35.377 46.3896 35.303 46.4713 35.1551C46.553 35.0071 46.5956 34.7807 46.5991 34.4759V33.5508Z"
                                    fill="white"
                                  ></path>
                                  <path
                                    d="M49.6934 35.9465H48.94V32.9679L48.0407 33.254V32.6257L49.6126 32.0481H49.6934V35.9465Z"
                                    fill="white"
                                  ></path>
                                  <path
                                    d="M54.0886 35.9465H53.3353V32.9679L52.4359 33.254V32.6257L54.0078 32.0481H54.0886V35.9465Z"
                                    fill="white"
                                  ></path>
                                  <path
                                    d="M57.926 35.9465H55.3243V35.4171L56.5521 34.0749C56.7207 33.8859 56.845 33.721 56.9249 33.5802C57.0066 33.4394 57.0474 33.3057 57.0474 33.1791C57.0474 33.0062 57.0049 32.8708 56.9197 32.7727C56.8345 32.6729 56.7129 32.623 56.5547 32.623C56.3844 32.623 56.2497 32.6836 56.1507 32.8048C56.0534 32.9242 56.0047 33.082 56.0047 33.2781H55.2487C55.2487 33.041 55.3034 32.8244 55.4129 32.6283C55.5242 32.4323 55.6806 32.279 55.8822 32.1684C56.0838 32.0561 56.3123 32 56.5678 32C56.9588 32 57.2621 32.0963 57.4776 32.2888C57.6948 32.4813 57.8034 32.7531 57.8034 33.1043C57.8034 33.2968 57.7548 33.4929 57.6575 33.6925C57.5601 33.8922 57.3933 34.1248 57.1569 34.3904L56.2941 35.3235H57.926V35.9465Z"
                                    fill="white"
                                  ></path>
                                  <path
                                    d="M60.22 35.9465H59.4666V32.9679L58.5673 33.254V32.6257L60.1392 32.0481H60.22V35.9465Z"
                                    fill="white"
                                  ></path>
                                  <path
                                    d="M62.2221 33.6578H62.6236C62.8147 33.6578 62.9564 33.6087 63.0485 33.5107C63.1406 33.4127 63.1867 33.2825 63.1867 33.1203C63.1867 32.9635 63.1406 32.8414 63.0485 32.754C62.9581 32.6667 62.833 32.623 62.6731 32.623C62.5289 32.623 62.4081 32.664 62.3107 32.746C62.2134 32.8262 62.1648 32.9314 62.1648 33.0615H61.4114C61.4114 32.8583 61.4644 32.6765 61.5704 32.516C61.6781 32.3538 61.8276 32.2273 62.0188 32.1364C62.2117 32.0455 62.4237 32 62.6549 32C63.0563 32 63.3709 32.0989 63.5985 32.2968C63.8262 32.4929 63.94 32.7638 63.94 33.1096C63.94 33.2879 63.887 33.4519 63.781 33.6016C63.675 33.7513 63.536 33.8663 63.3639 33.9465C63.5777 34.025 63.7367 34.1426 63.841 34.2995C63.947 34.4563 64 34.6417 64 34.8556C64 35.2014 63.8766 35.4786 63.6298 35.6872C63.3848 35.8957 63.0598 36 62.6549 36C62.276 36 61.9658 35.8975 61.7242 35.6925C61.4844 35.4875 61.3644 35.2166 61.3644 34.8797H62.1178C62.1178 35.0258 62.1708 35.1453 62.2769 35.238C62.3846 35.3307 62.5167 35.377 62.6731 35.377C62.8521 35.377 62.992 35.3289 63.0928 35.2326C63.1953 35.1346 63.2466 35.0053 63.2466 34.8449C63.2466 34.4563 63.0381 34.262 62.621 34.262H62.2221V33.6578Z"
                                    fill="white"
                                  ></path>
                                  <path
                                    d="M60 9.72821C60 8.22146 61.2215 7 62.7282 7H63.906V9.72821H60Z"
                                    fill="white"
                                  ></path>
                                  <path
                                    d="M60 17.1526C60 18.6594 61.2215 19.8809 62.7282 19.8809L63.9805 19.8809L63.9805 17.1526L60 17.1526Z"
                                    fill="white"
                                  ></path>
                                  <path
                                    d="M73 9.72821C73 8.22146 71.7785 7 70.2718 7L64.7259 7L64.7259 9.72821L73 9.72821Z"
                                    fill="white"
                                  ></path>
                                  <path d="M60 16L64 16L64 14L60 14L60 16Z" fill="white"></path>
                                  <path d="M60 13L64 13L64 11L60 11L60 13Z" fill="white"></path>
                                  <path
                                    d="M72.9849 17.1526C72.9849 18.6594 71.7634 19.8809 70.2567 19.8809L69.0789 19.8809L69.0789 17.1526L72.9849 17.1526Z"
                                    fill="white"
                                  ></path>
                                  <path d="M73 11L69 11L69 13L73 13L73 11Z" fill="white"></path>
                                  <path d="M73 14L69 14L69 16L73 16L73 14Z" fill="white"></path>
                                  <rect
                                    x="64.7261"
                                    y="7.12085"
                                    width="3.53326"
                                    height="12.7615"
                                    fill="white"
                                  ></rect>
                                </svg>
                                <div style="margin: 15px 5px">
                                  <a loading="0" href="/subscribe" class="sc-furwcr ejyCsp"
                                    >Upgrade to PREMIUM</a
                                  >
                                </div>
                              </div>
                            </b-card>
                          </b-col>
                        </b-row>
                        <br />
                        <b-row>
                          <b-col>
                            <b-card>
                              <div class="sc-khQegj sc-nVkyK dlKcPR ePhxwe">
                                <h4 size="16" class="sc-efQSVx iIffAV">Billing history</h4>
                                <table class="sc-jKjTWZ erurUF">
                                  <thead>
                                    <tr>
                                      <th>Type</th>
                                      <th>Invoice date</th>
                                      <th class="center">Amount</th>
                                      <th class="right">Status</th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    <tr>
                                      <td>Recurring</td>
                                      <td>January 3rd 2021</td>
                                      <td class="center">
                                        <span style="text-decoration: line-through">$49.00</span
                                        >&nbsp;<span>($0.00 adjusted)</span>
                                      </td>
                                      <td class="right">
                                        <div type="success" class="sc-ZOtfp fcDikN">Paid</div>
                                      </td>
                                    </tr>
                                    <tr>
                                      <td>Recurring</td>
                                      <td>December 3rd 2020</td>
                                      <td class="center">
                                        <span style="text-decoration: line-through">$49.00</span
                                        >&nbsp;<span>($0.00 adjusted)</span>
                                      </td>
                                      <td class="right">
                                        <div type="success" class="sc-ZOtfp fcDikN">Paid</div>
                                      </td>
                                    </tr>
                                    <tr>
                                      <td>Recurring</td>
                                      <td>November 3rd 2020</td>
                                      <td class="center">
                                        <span style="text-decoration: line-through">$49.00</span
                                        >&nbsp;<span>($0.00 adjusted)</span>
                                      </td>
                                      <td class="right">
                                        <div type="success" class="sc-ZOtfp fcDikN">Paid</div>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                                <div class="sc-ehCJOs jNbSbr">
                                  <a href="/v2/settings/account-and-billing/history"
                                    >Billing history</a
                                  >
                                </div>
                              </div>
                            </b-card>
                          </b-col>
                        </b-row>
                      </b-col>
                      <b-col cols="6">
                        <div class="sc-gYvZas iPBefu">
                          <b-card
                            style="border-radius: 15px; position: relative; text-align: center"
                          >
                            <h2 size="25" class="sc-iUKqMP sc-cvMrAr DCjDr jiNQBy">
                              You can do more with <b>PRO</b> for only $49 a month
                            </h2>
                            <div class="sc-khQegj sc-nVkyK dlKcPR ePhxwe sc-jwcQBs eLzmYs">
                              <div class="sc-eBHJIF jOpLsT">
                                <svg
                                  width="19"
                                  height="15"
                                  viewBox="0 0 17 13"
                                  version="1.1"
                                  xmlns="http://www.w3.org/2000/svg"
                                  xmlns:xlink="http://www.w3.org/1999/xlink"
                                >
                                  <path
                                    d="M5.81105 12.59L0 6.7792L1.93685 4.84235L5.81105 8.7163L14.5271 0L16.464 1.93685L5.81105 12.59Z"
                                    fill="#1DC724"
                                  ></path>
                                </svg>
                                <p class="sc-jcFjpl ZGdfu">Marketplace</p>
                              </div>
                              <div class="sc-eBHJIF jOpLsT">
                                <svg
                                  width="19"
                                  height="15"
                                  viewBox="0 0 17 13"
                                  version="1.1"
                                  xmlns="http://www.w3.org/2000/svg"
                                  xmlns:xlink="http://www.w3.org/1999/xlink"
                                >
                                  <path
                                    d="M5.81105 12.59L0 6.7792L1.93685 4.84235L5.81105 8.7163L14.5271 0L16.464 1.93685L5.81105 12.59Z"
                                    fill="#1DC724"
                                  ></path>
                                </svg>
                                <p class="sc-jcFjpl ZGdfu">OTAs</p>
                              </div>
                              <div class="sc-eBHJIF jOpLsT">
                                <svg
                                  width="19"
                                  height="15"
                                  viewBox="0 0 17 13"
                                  version="1.1"
                                  xmlns="http://www.w3.org/2000/svg"
                                  xmlns:xlink="http://www.w3.org/1999/xlink"
                                >
                                  <path
                                    d="M5.81105 12.59L0 6.7792L1.93685 4.84235L5.81105 8.7163L14.5271 0L16.464 1.93685L5.81105 12.59Z"
                                    fill="#1DC724"
                                  ></path>
                                </svg>
                                <p class="sc-jcFjpl ZGdfu">Unlimited users</p>
                              </div>
                              <div class="sc-eBHJIF jOpLsT">
                                <svg
                                  width="19"
                                  height="15"
                                  viewBox="0 0 17 13"
                                  version="1.1"
                                  xmlns="http://www.w3.org/2000/svg"
                                  xmlns:xlink="http://www.w3.org/1999/xlink"
                                >
                                  <path
                                    d="M5.81105 12.59L0 6.7792L1.93685 4.84235L5.81105 8.7163L14.5271 0L16.464 1.93685L5.81105 12.59Z"
                                    fill="#1DC724"
                                  ></path>
                                </svg>
                                <p class="sc-jcFjpl ZGdfu">Web services</p>
                              </div>
                              <div class="sc-eBHJIF jOpLsT">
                                <svg
                                  width="19"
                                  height="15"
                                  viewBox="0 0 17 13"
                                  version="1.1"
                                  xmlns="http://www.w3.org/2000/svg"
                                  xmlns:xlink="http://www.w3.org/1999/xlink"
                                >
                                  <path
                                    d="M5.81105 12.59L0 6.7792L1.93685 4.84235L5.81105 8.7163L14.5271 0L16.464 1.93685L5.81105 12.59Z"
                                    fill="#1DC724"
                                  ></path>
                                </svg>
                                <p class="sc-jcFjpl ZGdfu">Websites</p>
                              </div>
                              <div class="sc-eBHJIF jOpLsT">
                                <svg
                                  width="19"
                                  height="15"
                                  viewBox="0 0 17 13"
                                  version="1.1"
                                  xmlns="http://www.w3.org/2000/svg"
                                  xmlns:xlink="http://www.w3.org/1999/xlink"
                                >
                                  <path
                                    d="M5.81105 12.59L0 6.7792L1.93685 4.84235L5.81105 8.7163L14.5271 0L16.464 1.93685L5.81105 12.59Z"
                                    fill="#1DC724"
                                  ></path>
                                </svg>
                                <p class="sc-jcFjpl ZGdfu">Widgets</p>
                              </div>
                              <div class="sc-eBHJIF jOpLsT">
                                <svg
                                  width="19"
                                  height="15"
                                  viewBox="0 0 17 13"
                                  version="1.1"
                                  xmlns="http://www.w3.org/2000/svg"
                                  xmlns:xlink="http://www.w3.org/1999/xlink"
                                >
                                  <path
                                    d="M5.81105 12.59L0 6.7792L1.93685 4.84235L5.81105 8.7163L14.5271 0L16.464 1.93685L5.81105 12.59Z"
                                    fill="#1DC724"
                                  ></path>
                                </svg>
                                <p class="sc-jcFjpl ZGdfu">Customer management</p>
                              </div>
                              <div class="sc-eBHJIF jOpLsT">
                                <svg
                                  width="19"
                                  height="15"
                                  viewBox="0 0 17 13"
                                  version="1.1"
                                  xmlns="http://www.w3.org/2000/svg"
                                  xmlns:xlink="http://www.w3.org/1999/xlink"
                                >
                                  <path
                                    d="M5.81105 12.59L0 6.7792L1.93685 4.84235L5.81105 8.7163L14.5271 0L16.464 1.93685L5.81105 12.59Z"
                                    fill="#1DC724"
                                  ></path>
                                </svg>
                                <p class="sc-jcFjpl ZGdfu">Google Things to do</p>
                              </div>
                            </div>
                            <b-button loading="0" to="/subscribe" class="sc-furwcr lkUTuA"
                              >Upgrade to PREMIUM</b-button
                            >
                            <div style="margin-top: 16px">
                              <a href="https://www.bokun.io/pricing" class="sc-dPiLbb fuQCIy"
                                >Learn more</a
                              >
                            </div>
                          </b-card>
                        </div>
                      </b-col>
                    </b-row>
                  </div>
                </b-tab>
                <b-tab title="Billing history">
                  <table class="table table-hover">
                    <tbody>
                      <tr>
                        <td>Type: Recurring</td>
                        <td>
                          <p>Invoice date:</p>
                          <p>date of payment</p>
                        </td>
                        <td>
                          <p>Amount:</p>
                          <p>999.00$</p>
                        </td>
                        <td>
                          <p>Status:</p>
                          <p>Paid/declined/refunded ???</p>
                        </td>
                        <td>
                          <b-button variant="outline-secondary">Download</b-button>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </b-tab>
              </b-tabs>
            </b-col>
          </b-row>
        </b-card>
      </b-tab>


      <b-tab title="New Payment ">
        <div class="mt-5">
        <div class="row row-cols-1 row-cols-md-3 g-3 ">

            <PakageItem  v-for="p in pakages" :key="p.id"
            :pakage="p"
            />
          </div>
        </div>

      </b-tab>
    </b-tabs>
    <b-row> </b-row>
  </div>
</template>
<script>
import fixedPlugin from "../layout/FixedPlugin.vue";
import jwtInterceptor from '../../store/modules/jwtInterceptor'
// import PPakage from "./PPakage.vue";
import PakageItem from './PakageItem.vue';

export default {
  data() {
    return {
      pakages:[],
      themeChanger: false,
      showModal: false,
      changePasswordMod: false,
      twoFAModal: false,
      themeColor: "",
      company: {
        company: "",
        address: "",
        contactNumber: "",
        logo: "",
      },
      userInfo: {},
      genuine: false,
      premium: false,
      preferences: {},
    };
  },
  created() {
    this.getCompany();
    this.getPreferences();
    this.getUser();
    this.getGenuine();
    this.getPremium();
    this.loadPakages()
  },
  // eslint-disable-next-line vue/no-unused-components
  components: { fixedPlugin,PakageItem },
  computed: {
    isAuthenticated() {
      return this.$store.getters["user/isAuthenticated"];
    },
    planText() {
      return this.preferences.plan === "P" ? "Pro" : "Free";
    },
    moderate() {
      const keyValue = this.preferences.overridingModeration;
      const dict = {
        null: "Undefined",
        M: "Minimum",
        R: "Reasonable",
        D: "Moderate",
        A: "Advanced",
        O: "Open",
      };
      return dict[keyValue];
    },
    accountType() {
      return this.$store.getters["user/getUserType"];
    },
  },
  methods: {
    async loadPakages(){
                await jwtInterceptor.get('api/payments/packages/')
                    .then((res) => {
                        this.pakages = res.data.results
                    })
                    .catch((err) => {
                        console.log('Packages', err)
                    })
                },

    convertBool(value) {
      return value ? "Yes" : "No";
    },
    mail(value) {
      return value ? "" : "Don't ";
    },
    layout(value) {
      const dict = {
        null: "Undefined",
        F: "Facts points",
        R: "Rich text",
        G: "Grouped facts",
        S: "Summarized",
      };
      return dict[value];
    },
    getCompany() {
      this.$store
        .dispatch("settings/retrieveCompany")
        // eslint-disable-next-line no-unused-vars
        .then((response) => {
          /* console.log(response); */
          this.company = this.$store.getters["settings/getCompany"];
        })
        // eslint-disable-next-line no-unused-vars
        .catch((error) => {
          /* console.log(error); */
        });
    },
    getPreferences() {
      this.$store
        .dispatch("settings/retrievePreferences")
        // eslint-disable-next-line no-unused-vars
        .then((response) => {
          /* console.log(response); */
          this.preferences = this.$store.getters["settings/getPreferences"];
        })
        // eslint-disable-next-line no-unused-vars
        .catch((error) => {
          /* console.log(error); */
        });
    },
    getUser() {
      this.$store
        .dispatch("user/retrieveUserData")
        // eslint-disable-next-line no-unused-vars
        .then((response) => {
          /* console.log(response); */
          this.userInfo = this.$store.getters["user/userEmail"];
        })
        // eslint-disable-next-line no-unused-vars
        .catch((error) => {
          /* console.log(error); */
        });
    },
    getGenuine() {
      this.$store
        .dispatch("user/retrieveUserData")
        // eslint-disable-next-line no-unused-vars
        .then((response) => {
          /* console.log(response); */
          this.genuine = this.$store.getters["user/isGenuine"];
        })
        // eslint-disable-next-line no-unused-vars
        .catch((error) => {
          /* console.log(error); */
        });
    },
    getPremium() {
      this.$store
        .dispatch("user/retrieveUserData")
        // eslint-disable-next-line no-unused-vars
        .then((response) => {
          /* console.log(response); */
          this.premium = this.$store.getters["user/isPremium"];
        })
        // eslint-disable-next-line no-unused-vars
        .catch((error) => {
          /* console.log(error); */
        });
    },
    enableTwoFA() {
      this.twoFAModal = true;
    },
    changePasswordPop() {
      this.changePasswordMod = true;
    },
    async save() {
      if (this.propertyToEdit.id === 0) {
        await this.AddProperty();
      } else {
        await this.updateProperty();
      }
      this.showModal = false;
    },
    cancelTwoFA() {
      this.showModal = false;
      this.changePasswordMod = false;
    },
    changeTheme() {
      this.themeChanger = true;
    },
    saveTheme() {
      this.themeChanger = false;
    },
  },
};
</script>
