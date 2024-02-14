post_authorization_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "integer"
    },
    "error": {
      "type": "null"
    },
    "payload": {
      "type": "object",
      "properties": {
        "data": {
          "type": "object",
          "properties": {
            "sid": {
              "type": "string"
            }
          },
          "required": [
            "sid"
          ]
        }
      },
      "required": [
        "data"
      ]
    }
  },
  "required": [
    "status",
    "error",
    "payload"
  ]
}

put_add_books_to_cart = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "integer"
    },
    "error": {
      "type": "null"
    },
    "payload": {
      "type": "object",
      "properties": {
        "data": {
          "type": "object",
          "properties": {
            "added_art_ids": {
              "type": "array",
              "items": [
                {
                  "type": "integer"
                }
              ]
            },
            "failed_art_ids": {
              "type": "array",
              "items": {}
            }
          },
          "required": [
            "added_art_ids",
            "failed_art_ids"
          ]
        }
      },
      "required": [
        "data"
      ]
    }
  },
  "required": [
    "status",
    "error",
    "payload"
  ]
}

get_search_book = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "integer"
    },
    "error": {
      "type": "null"
    },
    "payload": {
      "type": "object",
      "properties": {
        "data": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "type": {
                  "type": "string"
                },
                "instance": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer"
                    },
                    "uuid": {
                      "type": "string"
                    },
                    "cover_url": {
                      "type": "string"
                    },
                    "url": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "cover_ratio": {
                      "type": "number"
                    },
                    "is_draft": {
                      "type": "boolean"
                    },
                    "art_type": {
                      "type": "integer"
                    },
                    "prices": {
                      "type": "object",
                      "properties": {
                        "final_price": {
                          "type": "number"
                        },
                        "inapp_price": {
                          "type": "null"
                        },
                        "inapp_base_price": {
                          "type": "null"
                        },
                        "full_price": {
                          "type": "number"
                        },
                        "discount_price": {
                          "type": "null"
                        },
                        "litcoin_count": {
                          "type": "integer"
                        },
                        "inapp_name": {
                          "type": "null"
                        },
                        "inapp_base_name": {
                          "type": "null"
                        },
                        "currency": {
                          "type": "string"
                        },
                        "discount_percent": {
                          "type": "null"
                        },
                        "cost_with_bonus": {
                          "type": "number"
                        },
                        "bonus_money": {
                          "type": "number"
                        },
                        "account_money": {
                          "type": "number"
                        },
                        "can_be_paid_by_account_money": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "final_price",
                        "inapp_price",
                        "inapp_base_price",
                        "full_price",
                        "discount_price",
                        "litcoin_count",
                        "inapp_name",
                        "inapp_base_name",
                        "currency",
                        "discount_percent",
                        "cost_with_bonus",
                        "bonus_money",
                        "account_money",
                        "can_be_paid_by_account_money"
                      ]
                    },
                    "is_auto_speech_gift": {
                      "type": "boolean"
                    },
                    "subtitle": {
                      "type": "string"
                    },
                    "min_age": {
                      "type": "integer"
                    },
                    "is_adult_content": {
                      "type": "boolean"
                    },
                    "cover_height": {
                      "type": "integer"
                    },
                    "cover_width": {
                      "type": "integer"
                    },
                    "foreign_publisher_id": {
                      "type": "null"
                    },
                    "language_code": {
                      "type": "string"
                    },
                    "symbols_count": {
                      "type": "integer"
                    },
                    "expected_symbols_count": {
                      "type": "null"
                    },
                    "podcast_serial_number": {
                      "type": "null"
                    },
                    "last_updated_at": {
                      "type": "string"
                    },
                    "last_released_at": {
                      "type": "string"
                    },
                    "read_percent": {
                      "type": "integer"
                    },
                    "is_finished": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_promo": {
                      "type": "boolean"
                    },
                    "advertising_marking": {
                      "type": "null"
                    },
                    "event_data": {
                      "type": "null"
                    },
                    "my_art_status": {
                      "type": "integer"
                    },
                    "is_subscription_art": {
                      "type": "boolean"
                    },
                    "is_available_with_subscription": {
                      "type": "boolean"
                    },
                    "is_available_with_litres_subscription": {
                      "type": "boolean"
                    },
                    "availability_with_partner_subscriptions": {
                      "type": "array",
                      "items": {}
                    },
                    "art_subscription_status_for_user": {
                      "type": "string"
                    },
                    "is_abonement_art": {
                      "type": "boolean"
                    },
                    "is_available_with_abonement": {
                      "type": "boolean"
                    },
                    "can_be_preordered": {
                      "type": "boolean"
                    },
                    "is_preorder_notified_for_user": {
                      "type": "boolean"
                    },
                    "is_exclusive_abonement": {
                      "type": "boolean"
                    },
                    "is_drm": {
                      "type": "boolean"
                    },
                    "in_gifts": {
                      "type": "integer"
                    },
                    "is_fourth_art_gift": {
                      "type": "boolean"
                    },
                    "podcast_left_to_buy": {
                      "type": "null"
                    },
                    "availability": {
                      "type": "integer"
                    },
                    "available_from": {
                      "type": "string"
                    },
                    "library_information": {
                      "type": "null"
                    },
                    "persons": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "uuid": {
                              "type": "string"
                            },
                            "full_name": {
                              "type": "string"
                            },
                            "full_rodit": {
                              "type": "string"
                            },
                            "url": {
                              "type": "string"
                            },
                            "role": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "uuid",
                            "full_name",
                            "full_rodit",
                            "url",
                            "role"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "uuid": {
                              "type": "string"
                            },
                            "full_name": {
                              "type": "string"
                            },
                            "full_rodit": {
                              "type": "string"
                            },
                            "url": {
                              "type": "string"
                            },
                            "role": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "uuid",
                            "full_name",
                            "full_rodit",
                            "url",
                            "role"
                          ]
                        }
                      ]
                    },
                    "is_liked": {
                      "type": "boolean"
                    },
                    "rating": {
                      "type": "object",
                      "properties": {
                        "user_rating": {
                          "type": "null"
                        },
                        "rated_1_count": {
                          "type": "integer"
                        },
                        "rated_2_count": {
                          "type": "integer"
                        },
                        "rated_3_count": {
                          "type": "integer"
                        },
                        "rated_4_count": {
                          "type": "integer"
                        },
                        "rated_5_count": {
                          "type": "integer"
                        },
                        "rated_avg": {
                          "type": "number"
                        },
                        "rated_total_count": {
                          "type": "integer"
                        }
                      },
                      "required": [
                        "user_rating",
                        "rated_1_count",
                        "rated_2_count",
                        "rated_3_count",
                        "rated_4_count",
                        "rated_5_count",
                        "rated_avg",
                        "rated_total_count"
                      ]
                    },
                    "linked_arts": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "uuid": {
                              "type": "string"
                            },
                            "cover_url": {
                              "type": "string"
                            },
                            "url": {
                              "type": "string"
                            },
                            "title": {
                              "type": "string"
                            },
                            "cover_ratio": {
                              "type": "number"
                            },
                            "is_draft": {
                              "type": "boolean"
                            },
                            "art_type": {
                              "type": "integer"
                            },
                            "prices": {
                              "type": "object",
                              "properties": {
                                "final_price": {
                                  "type": "number"
                                },
                                "inapp_price": {
                                  "type": "null"
                                },
                                "inapp_base_price": {
                                  "type": "null"
                                },
                                "full_price": {
                                  "type": "number"
                                },
                                "discount_price": {
                                  "type": "null"
                                },
                                "litcoin_count": {
                                  "type": "integer"
                                },
                                "inapp_name": {
                                  "type": "null"
                                },
                                "inapp_base_name": {
                                  "type": "null"
                                },
                                "currency": {
                                  "type": "string"
                                },
                                "discount_percent": {
                                  "type": "null"
                                },
                                "cost_with_bonus": {
                                  "type": "number"
                                },
                                "bonus_money": {
                                  "type": "number"
                                },
                                "account_money": {
                                  "type": "number"
                                },
                                "can_be_paid_by_account_money": {
                                  "type": "boolean"
                                }
                              },
                              "required": [
                                "final_price",
                                "inapp_price",
                                "inapp_base_price",
                                "full_price",
                                "discount_price",
                                "litcoin_count",
                                "inapp_name",
                                "inapp_base_name",
                                "currency",
                                "discount_percent",
                                "cost_with_bonus",
                                "bonus_money",
                                "account_money",
                                "can_be_paid_by_account_money"
                              ]
                            },
                            "is_auto_speech_gift": {
                              "type": "boolean"
                            },
                            "availability": {
                              "type": "integer"
                            },
                            "is_free": {
                              "type": "boolean"
                            },
                            "persons": {
                              "type": "array",
                              "items": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "integer"
                                    },
                                    "uuid": {
                                      "type": "string"
                                    },
                                    "full_name": {
                                      "type": "string"
                                    },
                                    "full_rodit": {
                                      "type": "string"
                                    },
                                    "url": {
                                      "type": "string"
                                    },
                                    "role": {
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "uuid",
                                    "full_name",
                                    "full_rodit",
                                    "url",
                                    "role"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "integer"
                                    },
                                    "uuid": {
                                      "type": "string"
                                    },
                                    "full_name": {
                                      "type": "string"
                                    },
                                    "full_rodit": {
                                      "type": "string"
                                    },
                                    "url": {
                                      "type": "string"
                                    },
                                    "role": {
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "uuid",
                                    "full_name",
                                    "full_rodit",
                                    "url",
                                    "role"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "integer"
                                    },
                                    "uuid": {
                                      "type": "string"
                                    },
                                    "full_name": {
                                      "type": "string"
                                    },
                                    "full_rodit": {
                                      "type": "string"
                                    },
                                    "url": {
                                      "type": "string"
                                    },
                                    "role": {
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "uuid",
                                    "full_name",
                                    "full_rodit",
                                    "url",
                                    "role"
                                  ]
                                }
                              ]
                            },
                            "my_art_status": {
                              "type": "integer"
                            },
                            "is_subscription_art": {
                              "type": "boolean"
                            },
                            "is_available_with_subscription": {
                              "type": "boolean"
                            },
                            "library_information": {
                              "type": "null"
                            },
                            "release_file_id": {
                              "type": "integer"
                            },
                            "preview_file_id": {
                              "type": "integer"
                            },
                            "first_time_sale_at": {
                              "type": "string"
                            },
                            "linked_art_group": {
                              "type": "string"
                            },
                            "is_auto_speech": {
                              "type": "boolean"
                            },
                            "can_be_preordered": {
                              "type": "boolean"
                            },
                            "is_hidden": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "uuid",
                            "cover_url",
                            "url",
                            "title",
                            "cover_ratio",
                            "is_draft",
                            "art_type",
                            "prices",
                            "is_auto_speech_gift",
                            "availability",
                            "is_free",
                            "persons",
                            "my_art_status",
                            "is_subscription_art",
                            "is_available_with_subscription",
                            "library_information",
                            "release_file_id",
                            "preview_file_id",
                            "first_time_sale_at",
                            "linked_art_group",
                            "is_auto_speech",
                            "can_be_preordered",
                            "is_hidden"
                          ]
                        }
                      ]
                    },
                    "series": {
                      "type": "array",
                      "items": {}
                    },
                    "date_written_at": {
                      "type": "string"
                    },
                    "release_file_id": {
                      "type": "integer"
                    },
                    "preview_file_id": {
                      "type": "null"
                    },
                    "labels": {
                      "type": "object",
                      "properties": {
                        "is_bestseller": {
                          "type": "boolean"
                        },
                        "is_litres_exclusive": {
                          "type": "boolean"
                        },
                        "is_new": {
                          "type": "boolean"
                        },
                        "is_sales_hit": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "is_bestseller",
                        "is_litres_exclusive",
                        "is_new",
                        "is_sales_hit"
                      ]
                    },
                    "in_folders": {
                      "type": "null"
                    },
                    "is_archived": {
                      "type": "boolean"
                    },
                    "interacted_at": {
                      "type": "null"
                    },
                    "read_at": {
                      "type": "null"
                    },
                    "purchased_at": {
                      "type": "null"
                    },
                    "is_hidden": {
                      "type": "boolean"
                    },
                    "synchronized_arts": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "id"
                          ]
                        }
                      ]
                    },
                    "synchronizations": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "text_art_id": {
                              "type": "integer"
                            },
                            "audio_art_id": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "id",
                            "text_art_id",
                            "audio_art_id"
                          ]
                        }
                      ]
                    },
                    "alternative_version": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "integer"
                        },
                        "link_type": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "link_type"
                      ]
                    },
                    "in_user_cart_status": {
                      "type": "string"
                    },
                    "is_draft_full_free": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "id",
                    "uuid",
                    "cover_url",
                    "url",
                    "title",
                    "cover_ratio",
                    "is_draft",
                    "art_type",
                    "prices",
                    "is_auto_speech_gift",
                    "subtitle",
                    "min_age",
                    "is_adult_content",
                    "cover_height",
                    "cover_width",
                    "foreign_publisher_id",
                    "language_code",
                    "symbols_count",
                    "expected_symbols_count",
                    "podcast_serial_number",
                    "last_updated_at",
                    "last_released_at",
                    "read_percent",
                    "is_finished",
                    "is_free",
                    "is_promo",
                    "advertising_marking",
                    "event_data",
                    "my_art_status",
                    "is_subscription_art",
                    "is_available_with_subscription",
                    "is_available_with_litres_subscription",
                    "availability_with_partner_subscriptions",
                    "art_subscription_status_for_user",
                    "is_abonement_art",
                    "is_available_with_abonement",
                    "can_be_preordered",
                    "is_preorder_notified_for_user",
                    "is_exclusive_abonement",
                    "is_drm",
                    "in_gifts",
                    "is_fourth_art_gift",
                    "podcast_left_to_buy",
                    "availability",
                    "available_from",
                    "library_information",
                    "persons",
                    "is_liked",
                    "rating",
                    "linked_arts",
                    "series",
                    "date_written_at",
                    "release_file_id",
                    "preview_file_id",
                    "labels",
                    "in_folders",
                    "is_archived",
                    "interacted_at",
                    "read_at",
                    "purchased_at",
                    "is_hidden",
                    "synchronized_arts",
                    "synchronizations",
                    "alternative_version",
                    "in_user_cart_status",
                    "is_draft_full_free"
                  ]
                }
              },
              "required": [
                "type",
                "instance"
              ]
            },
            {
              "type": "object",
              "properties": {
                "type": {
                  "type": "string"
                },
                "instance": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer"
                    },
                    "uuid": {
                      "type": "string"
                    },
                    "cover_url": {
                      "type": "string"
                    },
                    "url": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "cover_ratio": {
                      "type": "number"
                    },
                    "is_draft": {
                      "type": "boolean"
                    },
                    "art_type": {
                      "type": "integer"
                    },
                    "prices": {
                      "type": "object",
                      "properties": {
                        "final_price": {
                          "type": "number"
                        },
                        "inapp_price": {
                          "type": "null"
                        },
                        "inapp_base_price": {
                          "type": "null"
                        },
                        "full_price": {
                          "type": "number"
                        },
                        "discount_price": {
                          "type": "null"
                        },
                        "litcoin_count": {
                          "type": "integer"
                        },
                        "inapp_name": {
                          "type": "null"
                        },
                        "inapp_base_name": {
                          "type": "null"
                        },
                        "currency": {
                          "type": "string"
                        },
                        "discount_percent": {
                          "type": "null"
                        },
                        "cost_with_bonus": {
                          "type": "number"
                        },
                        "bonus_money": {
                          "type": "number"
                        },
                        "account_money": {
                          "type": "number"
                        },
                        "can_be_paid_by_account_money": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "final_price",
                        "inapp_price",
                        "inapp_base_price",
                        "full_price",
                        "discount_price",
                        "litcoin_count",
                        "inapp_name",
                        "inapp_base_name",
                        "currency",
                        "discount_percent",
                        "cost_with_bonus",
                        "bonus_money",
                        "account_money",
                        "can_be_paid_by_account_money"
                      ]
                    },
                    "is_auto_speech_gift": {
                      "type": "boolean"
                    },
                    "subtitle": {
                      "type": "string"
                    },
                    "min_age": {
                      "type": "integer"
                    },
                    "is_adult_content": {
                      "type": "boolean"
                    },
                    "cover_height": {
                      "type": "integer"
                    },
                    "cover_width": {
                      "type": "integer"
                    },
                    "foreign_publisher_id": {
                      "type": "null"
                    },
                    "language_code": {
                      "type": "string"
                    },
                    "symbols_count": {
                      "type": "integer"
                    },
                    "expected_symbols_count": {
                      "type": "null"
                    },
                    "podcast_serial_number": {
                      "type": "null"
                    },
                    "last_updated_at": {
                      "type": "string"
                    },
                    "last_released_at": {
                      "type": "string"
                    },
                    "read_percent": {
                      "type": "integer"
                    },
                    "is_finished": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_promo": {
                      "type": "boolean"
                    },
                    "advertising_marking": {
                      "type": "null"
                    },
                    "event_data": {
                      "type": "null"
                    },
                    "my_art_status": {
                      "type": "integer"
                    },
                    "is_subscription_art": {
                      "type": "boolean"
                    },
                    "is_available_with_subscription": {
                      "type": "boolean"
                    },
                    "is_available_with_litres_subscription": {
                      "type": "boolean"
                    },
                    "availability_with_partner_subscriptions": {
                      "type": "array",
                      "items": {}
                    },
                    "art_subscription_status_for_user": {
                      "type": "string"
                    },
                    "is_abonement_art": {
                      "type": "boolean"
                    },
                    "is_available_with_abonement": {
                      "type": "boolean"
                    },
                    "can_be_preordered": {
                      "type": "boolean"
                    },
                    "is_preorder_notified_for_user": {
                      "type": "boolean"
                    },
                    "is_exclusive_abonement": {
                      "type": "boolean"
                    },
                    "is_drm": {
                      "type": "boolean"
                    },
                    "in_gifts": {
                      "type": "integer"
                    },
                    "is_fourth_art_gift": {
                      "type": "boolean"
                    },
                    "podcast_left_to_buy": {
                      "type": "null"
                    },
                    "availability": {
                      "type": "integer"
                    },
                    "available_from": {
                      "type": "string"
                    },
                    "library_information": {
                      "type": "null"
                    },
                    "persons": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "uuid": {
                              "type": "string"
                            },
                            "full_name": {
                              "type": "string"
                            },
                            "full_rodit": {
                              "type": "string"
                            },
                            "url": {
                              "type": "string"
                            },
                            "role": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "uuid",
                            "full_name",
                            "full_rodit",
                            "url",
                            "role"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "uuid": {
                              "type": "string"
                            },
                            "full_name": {
                              "type": "string"
                            },
                            "full_rodit": {
                              "type": "string"
                            },
                            "url": {
                              "type": "string"
                            },
                            "role": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "uuid",
                            "full_name",
                            "full_rodit",
                            "url",
                            "role"
                          ]
                        }
                      ]
                    },
                    "is_liked": {
                      "type": "boolean"
                    },
                    "rating": {
                      "type": "object",
                      "properties": {
                        "user_rating": {
                          "type": "null"
                        },
                        "rated_1_count": {
                          "type": "integer"
                        },
                        "rated_2_count": {
                          "type": "integer"
                        },
                        "rated_3_count": {
                          "type": "integer"
                        },
                        "rated_4_count": {
                          "type": "integer"
                        },
                        "rated_5_count": {
                          "type": "integer"
                        },
                        "rated_avg": {
                          "type": "number"
                        },
                        "rated_total_count": {
                          "type": "integer"
                        }
                      },
                      "required": [
                        "user_rating",
                        "rated_1_count",
                        "rated_2_count",
                        "rated_3_count",
                        "rated_4_count",
                        "rated_5_count",
                        "rated_avg",
                        "rated_total_count"
                      ]
                    },
                    "linked_arts": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "uuid": {
                              "type": "string"
                            },
                            "cover_url": {
                              "type": "string"
                            },
                            "url": {
                              "type": "string"
                            },
                            "title": {
                              "type": "string"
                            },
                            "cover_ratio": {
                              "type": "number"
                            },
                            "is_draft": {
                              "type": "boolean"
                            },
                            "art_type": {
                              "type": "integer"
                            },
                            "prices": {
                              "type": "object",
                              "properties": {
                                "final_price": {
                                  "type": "number"
                                },
                                "inapp_price": {
                                  "type": "null"
                                },
                                "inapp_base_price": {
                                  "type": "null"
                                },
                                "full_price": {
                                  "type": "number"
                                },
                                "discount_price": {
                                  "type": "null"
                                },
                                "litcoin_count": {
                                  "type": "integer"
                                },
                                "inapp_name": {
                                  "type": "null"
                                },
                                "inapp_base_name": {
                                  "type": "null"
                                },
                                "currency": {
                                  "type": "string"
                                },
                                "discount_percent": {
                                  "type": "null"
                                },
                                "cost_with_bonus": {
                                  "type": "number"
                                },
                                "bonus_money": {
                                  "type": "number"
                                },
                                "account_money": {
                                  "type": "number"
                                },
                                "can_be_paid_by_account_money": {
                                  "type": "boolean"
                                }
                              },
                              "required": [
                                "final_price",
                                "inapp_price",
                                "inapp_base_price",
                                "full_price",
                                "discount_price",
                                "litcoin_count",
                                "inapp_name",
                                "inapp_base_name",
                                "currency",
                                "discount_percent",
                                "cost_with_bonus",
                                "bonus_money",
                                "account_money",
                                "can_be_paid_by_account_money"
                              ]
                            },
                            "is_auto_speech_gift": {
                              "type": "boolean"
                            },
                            "availability": {
                              "type": "integer"
                            },
                            "is_free": {
                              "type": "boolean"
                            },
                            "persons": {
                              "type": "array",
                              "items": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "integer"
                                    },
                                    "uuid": {
                                      "type": "string"
                                    },
                                    "full_name": {
                                      "type": "string"
                                    },
                                    "full_rodit": {
                                      "type": "string"
                                    },
                                    "url": {
                                      "type": "string"
                                    },
                                    "role": {
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "uuid",
                                    "full_name",
                                    "full_rodit",
                                    "url",
                                    "role"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "integer"
                                    },
                                    "uuid": {
                                      "type": "string"
                                    },
                                    "full_name": {
                                      "type": "string"
                                    },
                                    "full_rodit": {
                                      "type": "string"
                                    },
                                    "url": {
                                      "type": "string"
                                    },
                                    "role": {
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "uuid",
                                    "full_name",
                                    "full_rodit",
                                    "url",
                                    "role"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "integer"
                                    },
                                    "uuid": {
                                      "type": "string"
                                    },
                                    "full_name": {
                                      "type": "string"
                                    },
                                    "full_rodit": {
                                      "type": "string"
                                    },
                                    "url": {
                                      "type": "string"
                                    },
                                    "role": {
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "uuid",
                                    "full_name",
                                    "full_rodit",
                                    "url",
                                    "role"
                                  ]
                                }
                              ]
                            },
                            "my_art_status": {
                              "type": "integer"
                            },
                            "is_subscription_art": {
                              "type": "boolean"
                            },
                            "is_available_with_subscription": {
                              "type": "boolean"
                            },
                            "library_information": {
                              "type": "null"
                            },
                            "release_file_id": {
                              "type": "integer"
                            },
                            "preview_file_id": {
                              "type": "integer"
                            },
                            "first_time_sale_at": {
                              "type": "string"
                            },
                            "linked_art_group": {
                              "type": "string"
                            },
                            "is_auto_speech": {
                              "type": "boolean"
                            },
                            "can_be_preordered": {
                              "type": "boolean"
                            },
                            "is_hidden": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "uuid",
                            "cover_url",
                            "url",
                            "title",
                            "cover_ratio",
                            "is_draft",
                            "art_type",
                            "prices",
                            "is_auto_speech_gift",
                            "availability",
                            "is_free",
                            "persons",
                            "my_art_status",
                            "is_subscription_art",
                            "is_available_with_subscription",
                            "library_information",
                            "release_file_id",
                            "preview_file_id",
                            "first_time_sale_at",
                            "linked_art_group",
                            "is_auto_speech",
                            "can_be_preordered",
                            "is_hidden"
                          ]
                        }
                      ]
                    },
                    "series": {
                      "type": "array",
                      "items": {}
                    },
                    "date_written_at": {
                      "type": "string"
                    },
                    "release_file_id": {
                      "type": "integer"
                    },
                    "preview_file_id": {
                      "type": "null"
                    },
                    "labels": {
                      "type": "object",
                      "properties": {
                        "is_bestseller": {
                          "type": "boolean"
                        },
                        "is_litres_exclusive": {
                          "type": "boolean"
                        },
                        "is_new": {
                          "type": "boolean"
                        },
                        "is_sales_hit": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "is_bestseller",
                        "is_litres_exclusive",
                        "is_new",
                        "is_sales_hit"
                      ]
                    },
                    "in_folders": {
                      "type": "null"
                    },
                    "is_archived": {
                      "type": "boolean"
                    },
                    "interacted_at": {
                      "type": "null"
                    },
                    "read_at": {
                      "type": "null"
                    },
                    "purchased_at": {
                      "type": "null"
                    },
                    "is_hidden": {
                      "type": "boolean"
                    },
                    "synchronized_arts": {
                      "type": "array",
                      "items": {}
                    },
                    "synchronizations": {
                      "type": "array",
                      "items": {}
                    },
                    "alternative_version": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "integer"
                        },
                        "link_type": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "link_type"
                      ]
                    },
                    "in_user_cart_status": {
                      "type": "string"
                    },
                    "is_draft_full_free": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "id",
                    "uuid",
                    "cover_url",
                    "url",
                    "title",
                    "cover_ratio",
                    "is_draft",
                    "art_type",
                    "prices",
                    "is_auto_speech_gift",
                    "subtitle",
                    "min_age",
                    "is_adult_content",
                    "cover_height",
                    "cover_width",
                    "foreign_publisher_id",
                    "language_code",
                    "symbols_count",
                    "expected_symbols_count",
                    "podcast_serial_number",
                    "last_updated_at",
                    "last_released_at",
                    "read_percent",
                    "is_finished",
                    "is_free",
                    "is_promo",
                    "advertising_marking",
                    "event_data",
                    "my_art_status",
                    "is_subscription_art",
                    "is_available_with_subscription",
                    "is_available_with_litres_subscription",
                    "availability_with_partner_subscriptions",
                    "art_subscription_status_for_user",
                    "is_abonement_art",
                    "is_available_with_abonement",
                    "can_be_preordered",
                    "is_preorder_notified_for_user",
                    "is_exclusive_abonement",
                    "is_drm",
                    "in_gifts",
                    "is_fourth_art_gift",
                    "podcast_left_to_buy",
                    "availability",
                    "available_from",
                    "library_information",
                    "persons",
                    "is_liked",
                    "rating",
                    "linked_arts",
                    "series",
                    "date_written_at",
                    "release_file_id",
                    "preview_file_id",
                    "labels",
                    "in_folders",
                    "is_archived",
                    "interacted_at",
                    "read_at",
                    "purchased_at",
                    "is_hidden",
                    "synchronized_arts",
                    "synchronizations",
                    "alternative_version",
                    "in_user_cart_status",
                    "is_draft_full_free"
                  ]
                }
              },
              "required": [
                "type",
                "instance"
              ]
            },
            {
              "type": "object",
              "properties": {
                "type": {
                  "type": "string"
                },
                "instance": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer"
                    },
                    "uuid": {
                      "type": "string"
                    },
                    "cover_url": {
                      "type": "string"
                    },
                    "url": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "cover_ratio": {
                      "type": "number"
                    },
                    "is_draft": {
                      "type": "boolean"
                    },
                    "art_type": {
                      "type": "integer"
                    },
                    "prices": {
                      "type": "object",
                      "properties": {
                        "final_price": {
                          "type": "number"
                        },
                        "inapp_price": {
                          "type": "null"
                        },
                        "inapp_base_price": {
                          "type": "null"
                        },
                        "full_price": {
                          "type": "number"
                        },
                        "discount_price": {
                          "type": "null"
                        },
                        "litcoin_count": {
                          "type": "integer"
                        },
                        "inapp_name": {
                          "type": "null"
                        },
                        "inapp_base_name": {
                          "type": "null"
                        },
                        "currency": {
                          "type": "string"
                        },
                        "discount_percent": {
                          "type": "null"
                        },
                        "cost_with_bonus": {
                          "type": "number"
                        },
                        "bonus_money": {
                          "type": "number"
                        },
                        "account_money": {
                          "type": "number"
                        },
                        "can_be_paid_by_account_money": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "final_price",
                        "inapp_price",
                        "inapp_base_price",
                        "full_price",
                        "discount_price",
                        "litcoin_count",
                        "inapp_name",
                        "inapp_base_name",
                        "currency",
                        "discount_percent",
                        "cost_with_bonus",
                        "bonus_money",
                        "account_money",
                        "can_be_paid_by_account_money"
                      ]
                    },
                    "is_auto_speech_gift": {
                      "type": "boolean"
                    },
                    "subtitle": {
                      "type": "string"
                    },
                    "min_age": {
                      "type": "integer"
                    },
                    "is_adult_content": {
                      "type": "boolean"
                    },
                    "cover_height": {
                      "type": "integer"
                    },
                    "cover_width": {
                      "type": "integer"
                    },
                    "foreign_publisher_id": {
                      "type": "null"
                    },
                    "language_code": {
                      "type": "string"
                    },
                    "symbols_count": {
                      "type": "integer"
                    },
                    "expected_symbols_count": {
                      "type": "null"
                    },
                    "podcast_serial_number": {
                      "type": "null"
                    },
                    "last_updated_at": {
                      "type": "string"
                    },
                    "last_released_at": {
                      "type": "string"
                    },
                    "read_percent": {
                      "type": "integer"
                    },
                    "is_finished": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_promo": {
                      "type": "boolean"
                    },
                    "advertising_marking": {
                      "type": "null"
                    },
                    "event_data": {
                      "type": "null"
                    },
                    "my_art_status": {
                      "type": "integer"
                    },
                    "is_subscription_art": {
                      "type": "boolean"
                    },
                    "is_available_with_subscription": {
                      "type": "boolean"
                    },
                    "is_available_with_litres_subscription": {
                      "type": "boolean"
                    },
                    "availability_with_partner_subscriptions": {
                      "type": "array",
                      "items": {}
                    },
                    "art_subscription_status_for_user": {
                      "type": "string"
                    },
                    "is_abonement_art": {
                      "type": "boolean"
                    },
                    "is_available_with_abonement": {
                      "type": "boolean"
                    },
                    "can_be_preordered": {
                      "type": "boolean"
                    },
                    "is_preorder_notified_for_user": {
                      "type": "boolean"
                    },
                    "is_exclusive_abonement": {
                      "type": "boolean"
                    },
                    "is_drm": {
                      "type": "boolean"
                    },
                    "in_gifts": {
                      "type": "integer"
                    },
                    "is_fourth_art_gift": {
                      "type": "boolean"
                    },
                    "podcast_left_to_buy": {
                      "type": "null"
                    },
                    "availability": {
                      "type": "integer"
                    },
                    "available_from": {
                      "type": "string"
                    },
                    "library_information": {
                      "type": "null"
                    },
                    "persons": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "uuid": {
                              "type": "string"
                            },
                            "full_name": {
                              "type": "string"
                            },
                            "full_rodit": {
                              "type": "string"
                            },
                            "url": {
                              "type": "string"
                            },
                            "role": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "uuid",
                            "full_name",
                            "full_rodit",
                            "url",
                            "role"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "uuid": {
                              "type": "string"
                            },
                            "full_name": {
                              "type": "string"
                            },
                            "full_rodit": {
                              "type": "string"
                            },
                            "url": {
                              "type": "string"
                            },
                            "role": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "uuid",
                            "full_name",
                            "full_rodit",
                            "url",
                            "role"
                          ]
                        }
                      ]
                    },
                    "is_liked": {
                      "type": "boolean"
                    },
                    "rating": {
                      "type": "object",
                      "properties": {
                        "user_rating": {
                          "type": "null"
                        },
                        "rated_1_count": {
                          "type": "integer"
                        },
                        "rated_2_count": {
                          "type": "integer"
                        },
                        "rated_3_count": {
                          "type": "integer"
                        },
                        "rated_4_count": {
                          "type": "integer"
                        },
                        "rated_5_count": {
                          "type": "integer"
                        },
                        "rated_avg": {
                          "type": "number"
                        },
                        "rated_total_count": {
                          "type": "integer"
                        }
                      },
                      "required": [
                        "user_rating",
                        "rated_1_count",
                        "rated_2_count",
                        "rated_3_count",
                        "rated_4_count",
                        "rated_5_count",
                        "rated_avg",
                        "rated_total_count"
                      ]
                    },
                    "linked_arts": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "uuid": {
                              "type": "string"
                            },
                            "cover_url": {
                              "type": "string"
                            },
                            "url": {
                              "type": "string"
                            },
                            "title": {
                              "type": "string"
                            },
                            "cover_ratio": {
                              "type": "number"
                            },
                            "is_draft": {
                              "type": "boolean"
                            },
                            "art_type": {
                              "type": "integer"
                            },
                            "prices": {
                              "type": "object",
                              "properties": {
                                "final_price": {
                                  "type": "number"
                                },
                                "inapp_price": {
                                  "type": "null"
                                },
                                "inapp_base_price": {
                                  "type": "null"
                                },
                                "full_price": {
                                  "type": "number"
                                },
                                "discount_price": {
                                  "type": "null"
                                },
                                "litcoin_count": {
                                  "type": "integer"
                                },
                                "inapp_name": {
                                  "type": "null"
                                },
                                "inapp_base_name": {
                                  "type": "null"
                                },
                                "currency": {
                                  "type": "string"
                                },
                                "discount_percent": {
                                  "type": "null"
                                },
                                "cost_with_bonus": {
                                  "type": "number"
                                },
                                "bonus_money": {
                                  "type": "number"
                                },
                                "account_money": {
                                  "type": "number"
                                },
                                "can_be_paid_by_account_money": {
                                  "type": "boolean"
                                }
                              },
                              "required": [
                                "final_price",
                                "inapp_price",
                                "inapp_base_price",
                                "full_price",
                                "discount_price",
                                "litcoin_count",
                                "inapp_name",
                                "inapp_base_name",
                                "currency",
                                "discount_percent",
                                "cost_with_bonus",
                                "bonus_money",
                                "account_money",
                                "can_be_paid_by_account_money"
                              ]
                            },
                            "is_auto_speech_gift": {
                              "type": "boolean"
                            },
                            "availability": {
                              "type": "integer"
                            },
                            "is_free": {
                              "type": "boolean"
                            },
                            "persons": {
                              "type": "array",
                              "items": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "integer"
                                    },
                                    "uuid": {
                                      "type": "string"
                                    },
                                    "full_name": {
                                      "type": "string"
                                    },
                                    "full_rodit": {
                                      "type": "string"
                                    },
                                    "url": {
                                      "type": "string"
                                    },
                                    "role": {
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "uuid",
                                    "full_name",
                                    "full_rodit",
                                    "url",
                                    "role"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "integer"
                                    },
                                    "uuid": {
                                      "type": "string"
                                    },
                                    "full_name": {
                                      "type": "string"
                                    },
                                    "full_rodit": {
                                      "type": "string"
                                    },
                                    "url": {
                                      "type": "string"
                                    },
                                    "role": {
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "uuid",
                                    "full_name",
                                    "full_rodit",
                                    "url",
                                    "role"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "integer"
                                    },
                                    "uuid": {
                                      "type": "string"
                                    },
                                    "full_name": {
                                      "type": "string"
                                    },
                                    "full_rodit": {
                                      "type": "string"
                                    },
                                    "url": {
                                      "type": "string"
                                    },
                                    "role": {
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "uuid",
                                    "full_name",
                                    "full_rodit",
                                    "url",
                                    "role"
                                  ]
                                }
                              ]
                            },
                            "my_art_status": {
                              "type": "integer"
                            },
                            "is_subscription_art": {
                              "type": "boolean"
                            },
                            "is_available_with_subscription": {
                              "type": "boolean"
                            },
                            "library_information": {
                              "type": "null"
                            },
                            "release_file_id": {
                              "type": "integer"
                            },
                            "preview_file_id": {
                              "type": "integer"
                            },
                            "first_time_sale_at": {
                              "type": "string"
                            },
                            "linked_art_group": {
                              "type": "string"
                            },
                            "is_auto_speech": {
                              "type": "boolean"
                            },
                            "can_be_preordered": {
                              "type": "boolean"
                            },
                            "is_hidden": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "uuid",
                            "cover_url",
                            "url",
                            "title",
                            "cover_ratio",
                            "is_draft",
                            "art_type",
                            "prices",
                            "is_auto_speech_gift",
                            "availability",
                            "is_free",
                            "persons",
                            "my_art_status",
                            "is_subscription_art",
                            "is_available_with_subscription",
                            "library_information",
                            "release_file_id",
                            "preview_file_id",
                            "first_time_sale_at",
                            "linked_art_group",
                            "is_auto_speech",
                            "can_be_preordered",
                            "is_hidden"
                          ]
                        }
                      ]
                    },
                    "series": {
                      "type": "array",
                      "items": {}
                    },
                    "date_written_at": {
                      "type": "string"
                    },
                    "release_file_id": {
                      "type": "integer"
                    },
                    "preview_file_id": {
                      "type": "null"
                    },
                    "labels": {
                      "type": "object",
                      "properties": {
                        "is_bestseller": {
                          "type": "boolean"
                        },
                        "is_litres_exclusive": {
                          "type": "boolean"
                        },
                        "is_new": {
                          "type": "boolean"
                        },
                        "is_sales_hit": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "is_bestseller",
                        "is_litres_exclusive",
                        "is_new",
                        "is_sales_hit"
                      ]
                    },
                    "in_folders": {
                      "type": "null"
                    },
                    "is_archived": {
                      "type": "boolean"
                    },
                    "interacted_at": {
                      "type": "null"
                    },
                    "read_at": {
                      "type": "null"
                    },
                    "purchased_at": {
                      "type": "null"
                    },
                    "is_hidden": {
                      "type": "boolean"
                    },
                    "synchronized_arts": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "id"
                          ]
                        }
                      ]
                    },
                    "synchronizations": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "text_art_id": {
                              "type": "integer"
                            },
                            "audio_art_id": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "id",
                            "text_art_id",
                            "audio_art_id"
                          ]
                        }
                      ]
                    },
                    "alternative_version": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "integer"
                        },
                        "link_type": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "link_type"
                      ]
                    },
                    "in_user_cart_status": {
                      "type": "string"
                    },
                    "is_draft_full_free": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "id",
                    "uuid",
                    "cover_url",
                    "url",
                    "title",
                    "cover_ratio",
                    "is_draft",
                    "art_type",
                    "prices",
                    "is_auto_speech_gift",
                    "subtitle",
                    "min_age",
                    "is_adult_content",
                    "cover_height",
                    "cover_width",
                    "foreign_publisher_id",
                    "language_code",
                    "symbols_count",
                    "expected_symbols_count",
                    "podcast_serial_number",
                    "last_updated_at",
                    "last_released_at",
                    "read_percent",
                    "is_finished",
                    "is_free",
                    "is_promo",
                    "advertising_marking",
                    "event_data",
                    "my_art_status",
                    "is_subscription_art",
                    "is_available_with_subscription",
                    "is_available_with_litres_subscription",
                    "availability_with_partner_subscriptions",
                    "art_subscription_status_for_user",
                    "is_abonement_art",
                    "is_available_with_abonement",
                    "can_be_preordered",
                    "is_preorder_notified_for_user",
                    "is_exclusive_abonement",
                    "is_drm",
                    "in_gifts",
                    "is_fourth_art_gift",
                    "podcast_left_to_buy",
                    "availability",
                    "available_from",
                    "library_information",
                    "persons",
                    "is_liked",
                    "rating",
                    "linked_arts",
                    "series",
                    "date_written_at",
                    "release_file_id",
                    "preview_file_id",
                    "labels",
                    "in_folders",
                    "is_archived",
                    "interacted_at",
                    "read_at",
                    "purchased_at",
                    "is_hidden",
                    "synchronized_arts",
                    "synchronizations",
                    "alternative_version",
                    "in_user_cart_status",
                    "is_draft_full_free"
                  ]
                }
              },
              "required": [
                "type",
                "instance"
              ]
            },
            {
              "type": "object",
              "properties": {
                "type": {
                  "type": "string"
                },
                "instance": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer"
                    },
                    "uuid": {
                      "type": "string"
                    },
                    "cover_url": {
                      "type": "string"
                    },
                    "url": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "cover_ratio": {
                      "type": "number"
                    },
                    "is_draft": {
                      "type": "boolean"
                    },
                    "art_type": {
                      "type": "integer"
                    },
                    "prices": {
                      "type": "object",
                      "properties": {
                        "final_price": {
                          "type": "number"
                        },
                        "inapp_price": {
                          "type": "null"
                        },
                        "inapp_base_price": {
                          "type": "null"
                        },
                        "full_price": {
                          "type": "number"
                        },
                        "discount_price": {
                          "type": "null"
                        },
                        "litcoin_count": {
                          "type": "integer"
                        },
                        "inapp_name": {
                          "type": "null"
                        },
                        "inapp_base_name": {
                          "type": "null"
                        },
                        "currency": {
                          "type": "string"
                        },
                        "discount_percent": {
                          "type": "null"
                        },
                        "cost_with_bonus": {
                          "type": "number"
                        },
                        "bonus_money": {
                          "type": "number"
                        },
                        "account_money": {
                          "type": "number"
                        },
                        "can_be_paid_by_account_money": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "final_price",
                        "inapp_price",
                        "inapp_base_price",
                        "full_price",
                        "discount_price",
                        "litcoin_count",
                        "inapp_name",
                        "inapp_base_name",
                        "currency",
                        "discount_percent",
                        "cost_with_bonus",
                        "bonus_money",
                        "account_money",
                        "can_be_paid_by_account_money"
                      ]
                    },
                    "is_auto_speech_gift": {
                      "type": "boolean"
                    },
                    "subtitle": {
                      "type": "string"
                    },
                    "min_age": {
                      "type": "integer"
                    },
                    "is_adult_content": {
                      "type": "boolean"
                    },
                    "cover_height": {
                      "type": "integer"
                    },
                    "cover_width": {
                      "type": "integer"
                    },
                    "foreign_publisher_id": {
                      "type": "null"
                    },
                    "language_code": {
                      "type": "string"
                    },
                    "symbols_count": {
                      "type": "integer"
                    },
                    "expected_symbols_count": {
                      "type": "null"
                    },
                    "podcast_serial_number": {
                      "type": "null"
                    },
                    "last_updated_at": {
                      "type": "string"
                    },
                    "last_released_at": {
                      "type": "string"
                    },
                    "read_percent": {
                      "type": "integer"
                    },
                    "is_finished": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_promo": {
                      "type": "boolean"
                    },
                    "advertising_marking": {
                      "type": "null"
                    },
                    "event_data": {
                      "type": "null"
                    },
                    "my_art_status": {
                      "type": "integer"
                    },
                    "is_subscription_art": {
                      "type": "boolean"
                    },
                    "is_available_with_subscription": {
                      "type": "boolean"
                    },
                    "is_available_with_litres_subscription": {
                      "type": "boolean"
                    },
                    "availability_with_partner_subscriptions": {
                      "type": "array",
                      "items": {}
                    },
                    "art_subscription_status_for_user": {
                      "type": "string"
                    },
                    "is_abonement_art": {
                      "type": "boolean"
                    },
                    "is_available_with_abonement": {
                      "type": "boolean"
                    },
                    "can_be_preordered": {
                      "type": "boolean"
                    },
                    "is_preorder_notified_for_user": {
                      "type": "boolean"
                    },
                    "is_exclusive_abonement": {
                      "type": "boolean"
                    },
                    "is_drm": {
                      "type": "boolean"
                    },
                    "in_gifts": {
                      "type": "integer"
                    },
                    "is_fourth_art_gift": {
                      "type": "boolean"
                    },
                    "podcast_left_to_buy": {
                      "type": "null"
                    },
                    "availability": {
                      "type": "integer"
                    },
                    "available_from": {
                      "type": "string"
                    },
                    "library_information": {
                      "type": "null"
                    },
                    "persons": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "uuid": {
                              "type": "string"
                            },
                            "full_name": {
                              "type": "string"
                            },
                            "full_rodit": {
                              "type": "string"
                            },
                            "url": {
                              "type": "string"
                            },
                            "role": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "uuid",
                            "full_name",
                            "full_rodit",
                            "url",
                            "role"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "uuid": {
                              "type": "string"
                            },
                            "full_name": {
                              "type": "string"
                            },
                            "full_rodit": {
                              "type": "string"
                            },
                            "url": {
                              "type": "string"
                            },
                            "role": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "uuid",
                            "full_name",
                            "full_rodit",
                            "url",
                            "role"
                          ]
                        }
                      ]
                    },
                    "is_liked": {
                      "type": "boolean"
                    },
                    "rating": {
                      "type": "object",
                      "properties": {
                        "user_rating": {
                          "type": "null"
                        },
                        "rated_1_count": {
                          "type": "integer"
                        },
                        "rated_2_count": {
                          "type": "integer"
                        },
                        "rated_3_count": {
                          "type": "integer"
                        },
                        "rated_4_count": {
                          "type": "integer"
                        },
                        "rated_5_count": {
                          "type": "integer"
                        },
                        "rated_avg": {
                          "type": "number"
                        },
                        "rated_total_count": {
                          "type": "integer"
                        }
                      },
                      "required": [
                        "user_rating",
                        "rated_1_count",
                        "rated_2_count",
                        "rated_3_count",
                        "rated_4_count",
                        "rated_5_count",
                        "rated_avg",
                        "rated_total_count"
                      ]
                    },
                    "linked_arts": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "uuid": {
                              "type": "string"
                            },
                            "cover_url": {
                              "type": "string"
                            },
                            "url": {
                              "type": "string"
                            },
                            "title": {
                              "type": "string"
                            },
                            "cover_ratio": {
                              "type": "number"
                            },
                            "is_draft": {
                              "type": "boolean"
                            },
                            "art_type": {
                              "type": "integer"
                            },
                            "prices": {
                              "type": "object",
                              "properties": {
                                "final_price": {
                                  "type": "number"
                                },
                                "inapp_price": {
                                  "type": "null"
                                },
                                "inapp_base_price": {
                                  "type": "null"
                                },
                                "full_price": {
                                  "type": "number"
                                },
                                "discount_price": {
                                  "type": "null"
                                },
                                "litcoin_count": {
                                  "type": "integer"
                                },
                                "inapp_name": {
                                  "type": "null"
                                },
                                "inapp_base_name": {
                                  "type": "null"
                                },
                                "currency": {
                                  "type": "string"
                                },
                                "discount_percent": {
                                  "type": "null"
                                },
                                "cost_with_bonus": {
                                  "type": "number"
                                },
                                "bonus_money": {
                                  "type": "number"
                                },
                                "account_money": {
                                  "type": "number"
                                },
                                "can_be_paid_by_account_money": {
                                  "type": "boolean"
                                }
                              },
                              "required": [
                                "final_price",
                                "inapp_price",
                                "inapp_base_price",
                                "full_price",
                                "discount_price",
                                "litcoin_count",
                                "inapp_name",
                                "inapp_base_name",
                                "currency",
                                "discount_percent",
                                "cost_with_bonus",
                                "bonus_money",
                                "account_money",
                                "can_be_paid_by_account_money"
                              ]
                            },
                            "is_auto_speech_gift": {
                              "type": "boolean"
                            },
                            "availability": {
                              "type": "integer"
                            },
                            "is_free": {
                              "type": "boolean"
                            },
                            "persons": {
                              "type": "array",
                              "items": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "integer"
                                    },
                                    "uuid": {
                                      "type": "string"
                                    },
                                    "full_name": {
                                      "type": "string"
                                    },
                                    "full_rodit": {
                                      "type": "string"
                                    },
                                    "url": {
                                      "type": "string"
                                    },
                                    "role": {
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "uuid",
                                    "full_name",
                                    "full_rodit",
                                    "url",
                                    "role"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "integer"
                                    },
                                    "uuid": {
                                      "type": "string"
                                    },
                                    "full_name": {
                                      "type": "string"
                                    },
                                    "full_rodit": {
                                      "type": "string"
                                    },
                                    "url": {
                                      "type": "string"
                                    },
                                    "role": {
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "uuid",
                                    "full_name",
                                    "full_rodit",
                                    "url",
                                    "role"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "integer"
                                    },
                                    "uuid": {
                                      "type": "string"
                                    },
                                    "full_name": {
                                      "type": "string"
                                    },
                                    "full_rodit": {
                                      "type": "string"
                                    },
                                    "url": {
                                      "type": "string"
                                    },
                                    "role": {
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "uuid",
                                    "full_name",
                                    "full_rodit",
                                    "url",
                                    "role"
                                  ]
                                }
                              ]
                            },
                            "my_art_status": {
                              "type": "integer"
                            },
                            "is_subscription_art": {
                              "type": "boolean"
                            },
                            "is_available_with_subscription": {
                              "type": "boolean"
                            },
                            "library_information": {
                              "type": "null"
                            },
                            "release_file_id": {
                              "type": "integer"
                            },
                            "preview_file_id": {
                              "type": "integer"
                            },
                            "first_time_sale_at": {
                              "type": "string"
                            },
                            "linked_art_group": {
                              "type": "string"
                            },
                            "is_auto_speech": {
                              "type": "boolean"
                            },
                            "can_be_preordered": {
                              "type": "boolean"
                            },
                            "is_hidden": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "uuid",
                            "cover_url",
                            "url",
                            "title",
                            "cover_ratio",
                            "is_draft",
                            "art_type",
                            "prices",
                            "is_auto_speech_gift",
                            "availability",
                            "is_free",
                            "persons",
                            "my_art_status",
                            "is_subscription_art",
                            "is_available_with_subscription",
                            "library_information",
                            "release_file_id",
                            "preview_file_id",
                            "first_time_sale_at",
                            "linked_art_group",
                            "is_auto_speech",
                            "can_be_preordered",
                            "is_hidden"
                          ]
                        }
                      ]
                    },
                    "series": {
                      "type": "array",
                      "items": {}
                    },
                    "date_written_at": {
                      "type": "string"
                    },
                    "release_file_id": {
                      "type": "integer"
                    },
                    "preview_file_id": {
                      "type": "null"
                    },
                    "labels": {
                      "type": "object",
                      "properties": {
                        "is_bestseller": {
                          "type": "boolean"
                        },
                        "is_litres_exclusive": {
                          "type": "boolean"
                        },
                        "is_new": {
                          "type": "boolean"
                        },
                        "is_sales_hit": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "is_bestseller",
                        "is_litres_exclusive",
                        "is_new",
                        "is_sales_hit"
                      ]
                    },
                    "in_folders": {
                      "type": "null"
                    },
                    "is_archived": {
                      "type": "boolean"
                    },
                    "interacted_at": {
                      "type": "null"
                    },
                    "read_at": {
                      "type": "null"
                    },
                    "purchased_at": {
                      "type": "null"
                    },
                    "is_hidden": {
                      "type": "boolean"
                    },
                    "synchronized_arts": {
                      "type": "array",
                      "items": {}
                    },
                    "synchronizations": {
                      "type": "array",
                      "items": {}
                    },
                    "alternative_version": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "integer"
                        },
                        "link_type": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "link_type"
                      ]
                    },
                    "in_user_cart_status": {
                      "type": "string"
                    },
                    "is_draft_full_free": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "id",
                    "uuid",
                    "cover_url",
                    "url",
                    "title",
                    "cover_ratio",
                    "is_draft",
                    "art_type",
                    "prices",
                    "is_auto_speech_gift",
                    "subtitle",
                    "min_age",
                    "is_adult_content",
                    "cover_height",
                    "cover_width",
                    "foreign_publisher_id",
                    "language_code",
                    "symbols_count",
                    "expected_symbols_count",
                    "podcast_serial_number",
                    "last_updated_at",
                    "last_released_at",
                    "read_percent",
                    "is_finished",
                    "is_free",
                    "is_promo",
                    "advertising_marking",
                    "event_data",
                    "my_art_status",
                    "is_subscription_art",
                    "is_available_with_subscription",
                    "is_available_with_litres_subscription",
                    "availability_with_partner_subscriptions",
                    "art_subscription_status_for_user",
                    "is_abonement_art",
                    "is_available_with_abonement",
                    "can_be_preordered",
                    "is_preorder_notified_for_user",
                    "is_exclusive_abonement",
                    "is_drm",
                    "in_gifts",
                    "is_fourth_art_gift",
                    "podcast_left_to_buy",
                    "availability",
                    "available_from",
                    "library_information",
                    "persons",
                    "is_liked",
                    "rating",
                    "linked_arts",
                    "series",
                    "date_written_at",
                    "release_file_id",
                    "preview_file_id",
                    "labels",
                    "in_folders",
                    "is_archived",
                    "interacted_at",
                    "read_at",
                    "purchased_at",
                    "is_hidden",
                    "synchronized_arts",
                    "synchronizations",
                    "alternative_version",
                    "in_user_cart_status",
                    "is_draft_full_free"
                  ]
                }
              },
              "required": [
                "type",
                "instance"
              ]
            },
            {
              "type": "object",
              "properties": {
                "type": {
                  "type": "string"
                },
                "instance": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer"
                    },
                    "uuid": {
                      "type": "string"
                    },
                    "cover_url": {
                      "type": "string"
                    },
                    "url": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "cover_ratio": {
                      "type": "number"
                    },
                    "is_draft": {
                      "type": "boolean"
                    },
                    "art_type": {
                      "type": "integer"
                    },
                    "prices": {
                      "type": "object",
                      "properties": {
                        "final_price": {
                          "type": "number"
                        },
                        "inapp_price": {
                          "type": "null"
                        },
                        "inapp_base_price": {
                          "type": "null"
                        },
                        "full_price": {
                          "type": "number"
                        },
                        "discount_price": {
                          "type": "null"
                        },
                        "litcoin_count": {
                          "type": "integer"
                        },
                        "inapp_name": {
                          "type": "null"
                        },
                        "inapp_base_name": {
                          "type": "null"
                        },
                        "currency": {
                          "type": "string"
                        },
                        "discount_percent": {
                          "type": "null"
                        },
                        "cost_with_bonus": {
                          "type": "number"
                        },
                        "bonus_money": {
                          "type": "number"
                        },
                        "account_money": {
                          "type": "number"
                        },
                        "can_be_paid_by_account_money": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "final_price",
                        "inapp_price",
                        "inapp_base_price",
                        "full_price",
                        "discount_price",
                        "litcoin_count",
                        "inapp_name",
                        "inapp_base_name",
                        "currency",
                        "discount_percent",
                        "cost_with_bonus",
                        "bonus_money",
                        "account_money",
                        "can_be_paid_by_account_money"
                      ]
                    },
                    "is_auto_speech_gift": {
                      "type": "boolean"
                    },
                    "subtitle": {
                      "type": "string"
                    },
                    "min_age": {
                      "type": "integer"
                    },
                    "is_adult_content": {
                      "type": "boolean"
                    },
                    "cover_height": {
                      "type": "integer"
                    },
                    "cover_width": {
                      "type": "integer"
                    },
                    "foreign_publisher_id": {
                      "type": "null"
                    },
                    "language_code": {
                      "type": "string"
                    },
                    "symbols_count": {
                      "type": "integer"
                    },
                    "expected_symbols_count": {
                      "type": "null"
                    },
                    "podcast_serial_number": {
                      "type": "null"
                    },
                    "last_updated_at": {
                      "type": "string"
                    },
                    "last_released_at": {
                      "type": "string"
                    },
                    "read_percent": {
                      "type": "integer"
                    },
                    "is_finished": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_promo": {
                      "type": "boolean"
                    },
                    "advertising_marking": {
                      "type": "null"
                    },
                    "event_data": {
                      "type": "null"
                    },
                    "my_art_status": {
                      "type": "integer"
                    },
                    "is_subscription_art": {
                      "type": "boolean"
                    },
                    "is_available_with_subscription": {
                      "type": "boolean"
                    },
                    "is_available_with_litres_subscription": {
                      "type": "boolean"
                    },
                    "availability_with_partner_subscriptions": {
                      "type": "array",
                      "items": {}
                    },
                    "art_subscription_status_for_user": {
                      "type": "string"
                    },
                    "is_abonement_art": {
                      "type": "boolean"
                    },
                    "is_available_with_abonement": {
                      "type": "boolean"
                    },
                    "can_be_preordered": {
                      "type": "boolean"
                    },
                    "is_preorder_notified_for_user": {
                      "type": "boolean"
                    },
                    "is_exclusive_abonement": {
                      "type": "boolean"
                    },
                    "is_drm": {
                      "type": "boolean"
                    },
                    "in_gifts": {
                      "type": "integer"
                    },
                    "is_fourth_art_gift": {
                      "type": "boolean"
                    },
                    "podcast_left_to_buy": {
                      "type": "null"
                    },
                    "availability": {
                      "type": "integer"
                    },
                    "available_from": {
                      "type": "string"
                    },
                    "library_information": {
                      "type": "null"
                    },
                    "persons": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "uuid": {
                              "type": "string"
                            },
                            "full_name": {
                              "type": "string"
                            },
                            "full_rodit": {
                              "type": "string"
                            },
                            "url": {
                              "type": "string"
                            },
                            "role": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "uuid",
                            "full_name",
                            "full_rodit",
                            "url",
                            "role"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "uuid": {
                              "type": "string"
                            },
                            "full_name": {
                              "type": "string"
                            },
                            "full_rodit": {
                              "type": "string"
                            },
                            "url": {
                              "type": "string"
                            },
                            "role": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "uuid",
                            "full_name",
                            "full_rodit",
                            "url",
                            "role"
                          ]
                        }
                      ]
                    },
                    "is_liked": {
                      "type": "boolean"
                    },
                    "rating": {
                      "type": "object",
                      "properties": {
                        "user_rating": {
                          "type": "null"
                        },
                        "rated_1_count": {
                          "type": "integer"
                        },
                        "rated_2_count": {
                          "type": "integer"
                        },
                        "rated_3_count": {
                          "type": "integer"
                        },
                        "rated_4_count": {
                          "type": "integer"
                        },
                        "rated_5_count": {
                          "type": "integer"
                        },
                        "rated_avg": {
                          "type": "number"
                        },
                        "rated_total_count": {
                          "type": "integer"
                        }
                      },
                      "required": [
                        "user_rating",
                        "rated_1_count",
                        "rated_2_count",
                        "rated_3_count",
                        "rated_4_count",
                        "rated_5_count",
                        "rated_avg",
                        "rated_total_count"
                      ]
                    },
                    "linked_arts": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "uuid": {
                              "type": "string"
                            },
                            "cover_url": {
                              "type": "string"
                            },
                            "url": {
                              "type": "string"
                            },
                            "title": {
                              "type": "string"
                            },
                            "cover_ratio": {
                              "type": "number"
                            },
                            "is_draft": {
                              "type": "boolean"
                            },
                            "art_type": {
                              "type": "integer"
                            },
                            "prices": {
                              "type": "object",
                              "properties": {
                                "final_price": {
                                  "type": "number"
                                },
                                "inapp_price": {
                                  "type": "null"
                                },
                                "inapp_base_price": {
                                  "type": "null"
                                },
                                "full_price": {
                                  "type": "number"
                                },
                                "discount_price": {
                                  "type": "null"
                                },
                                "litcoin_count": {
                                  "type": "integer"
                                },
                                "inapp_name": {
                                  "type": "null"
                                },
                                "inapp_base_name": {
                                  "type": "null"
                                },
                                "currency": {
                                  "type": "string"
                                },
                                "discount_percent": {
                                  "type": "null"
                                },
                                "cost_with_bonus": {
                                  "type": "number"
                                },
                                "bonus_money": {
                                  "type": "number"
                                },
                                "account_money": {
                                  "type": "number"
                                },
                                "can_be_paid_by_account_money": {
                                  "type": "boolean"
                                }
                              },
                              "required": [
                                "final_price",
                                "inapp_price",
                                "inapp_base_price",
                                "full_price",
                                "discount_price",
                                "litcoin_count",
                                "inapp_name",
                                "inapp_base_name",
                                "currency",
                                "discount_percent",
                                "cost_with_bonus",
                                "bonus_money",
                                "account_money",
                                "can_be_paid_by_account_money"
                              ]
                            },
                            "is_auto_speech_gift": {
                              "type": "boolean"
                            },
                            "availability": {
                              "type": "integer"
                            },
                            "is_free": {
                              "type": "boolean"
                            },
                            "persons": {
                              "type": "array",
                              "items": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "integer"
                                    },
                                    "uuid": {
                                      "type": "string"
                                    },
                                    "full_name": {
                                      "type": "string"
                                    },
                                    "full_rodit": {
                                      "type": "string"
                                    },
                                    "url": {
                                      "type": "string"
                                    },
                                    "role": {
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "uuid",
                                    "full_name",
                                    "full_rodit",
                                    "url",
                                    "role"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "integer"
                                    },
                                    "uuid": {
                                      "type": "string"
                                    },
                                    "full_name": {
                                      "type": "string"
                                    },
                                    "full_rodit": {
                                      "type": "string"
                                    },
                                    "url": {
                                      "type": "string"
                                    },
                                    "role": {
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "uuid",
                                    "full_name",
                                    "full_rodit",
                                    "url",
                                    "role"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "integer"
                                    },
                                    "uuid": {
                                      "type": "string"
                                    },
                                    "full_name": {
                                      "type": "string"
                                    },
                                    "full_rodit": {
                                      "type": "string"
                                    },
                                    "url": {
                                      "type": "string"
                                    },
                                    "role": {
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "uuid",
                                    "full_name",
                                    "full_rodit",
                                    "url",
                                    "role"
                                  ]
                                }
                              ]
                            },
                            "my_art_status": {
                              "type": "integer"
                            },
                            "is_subscription_art": {
                              "type": "boolean"
                            },
                            "is_available_with_subscription": {
                              "type": "boolean"
                            },
                            "library_information": {
                              "type": "null"
                            },
                            "release_file_id": {
                              "type": "integer"
                            },
                            "preview_file_id": {
                              "type": "integer"
                            },
                            "first_time_sale_at": {
                              "type": "string"
                            },
                            "linked_art_group": {
                              "type": "string"
                            },
                            "is_auto_speech": {
                              "type": "boolean"
                            },
                            "can_be_preordered": {
                              "type": "boolean"
                            },
                            "is_hidden": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "uuid",
                            "cover_url",
                            "url",
                            "title",
                            "cover_ratio",
                            "is_draft",
                            "art_type",
                            "prices",
                            "is_auto_speech_gift",
                            "availability",
                            "is_free",
                            "persons",
                            "my_art_status",
                            "is_subscription_art",
                            "is_available_with_subscription",
                            "library_information",
                            "release_file_id",
                            "preview_file_id",
                            "first_time_sale_at",
                            "linked_art_group",
                            "is_auto_speech",
                            "can_be_preordered",
                            "is_hidden"
                          ]
                        }
                      ]
                    },
                    "series": {
                      "type": "array",
                      "items": {}
                    },
                    "date_written_at": {
                      "type": "string"
                    },
                    "release_file_id": {
                      "type": "integer"
                    },
                    "preview_file_id": {
                      "type": "null"
                    },
                    "labels": {
                      "type": "object",
                      "properties": {
                        "is_bestseller": {
                          "type": "boolean"
                        },
                        "is_litres_exclusive": {
                          "type": "boolean"
                        },
                        "is_new": {
                          "type": "boolean"
                        },
                        "is_sales_hit": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "is_bestseller",
                        "is_litres_exclusive",
                        "is_new",
                        "is_sales_hit"
                      ]
                    },
                    "in_folders": {
                      "type": "null"
                    },
                    "is_archived": {
                      "type": "boolean"
                    },
                    "interacted_at": {
                      "type": "null"
                    },
                    "read_at": {
                      "type": "null"
                    },
                    "purchased_at": {
                      "type": "null"
                    },
                    "is_hidden": {
                      "type": "boolean"
                    },
                    "synchronized_arts": {
                      "type": "array",
                      "items": {}
                    },
                    "synchronizations": {
                      "type": "array",
                      "items": {}
                    },
                    "alternative_version": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "integer"
                        },
                        "link_type": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "link_type"
                      ]
                    },
                    "in_user_cart_status": {
                      "type": "string"
                    },
                    "is_draft_full_free": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "id",
                    "uuid",
                    "cover_url",
                    "url",
                    "title",
                    "cover_ratio",
                    "is_draft",
                    "art_type",
                    "prices",
                    "is_auto_speech_gift",
                    "subtitle",
                    "min_age",
                    "is_adult_content",
                    "cover_height",
                    "cover_width",
                    "foreign_publisher_id",
                    "language_code",
                    "symbols_count",
                    "expected_symbols_count",
                    "podcast_serial_number",
                    "last_updated_at",
                    "last_released_at",
                    "read_percent",
                    "is_finished",
                    "is_free",
                    "is_promo",
                    "advertising_marking",
                    "event_data",
                    "my_art_status",
                    "is_subscription_art",
                    "is_available_with_subscription",
                    "is_available_with_litres_subscription",
                    "availability_with_partner_subscriptions",
                    "art_subscription_status_for_user",
                    "is_abonement_art",
                    "is_available_with_abonement",
                    "can_be_preordered",
                    "is_preorder_notified_for_user",
                    "is_exclusive_abonement",
                    "is_drm",
                    "in_gifts",
                    "is_fourth_art_gift",
                    "podcast_left_to_buy",
                    "availability",
                    "available_from",
                    "library_information",
                    "persons",
                    "is_liked",
                    "rating",
                    "linked_arts",
                    "series",
                    "date_written_at",
                    "release_file_id",
                    "preview_file_id",
                    "labels",
                    "in_folders",
                    "is_archived",
                    "interacted_at",
                    "read_at",
                    "purchased_at",
                    "is_hidden",
                    "synchronized_arts",
                    "synchronizations",
                    "alternative_version",
                    "in_user_cart_status",
                    "is_draft_full_free"
                  ]
                }
              },
              "required": [
                "type",
                "instance"
              ]
            },
            {
              "type": "object",
              "properties": {
                "type": {
                  "type": "string"
                },
                "instance": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer"
                    },
                    "uuid": {
                      "type": "string"
                    },
                    "cover_url": {
                      "type": "string"
                    },
                    "url": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "cover_ratio": {
                      "type": "number"
                    },
                    "is_draft": {
                      "type": "boolean"
                    },
                    "art_type": {
                      "type": "integer"
                    },
                    "prices": {
                      "type": "object",
                      "properties": {
                        "final_price": {
                          "type": "number"
                        },
                        "inapp_price": {
                          "type": "null"
                        },
                        "inapp_base_price": {
                          "type": "null"
                        },
                        "full_price": {
                          "type": "number"
                        },
                        "discount_price": {
                          "type": "null"
                        },
                        "litcoin_count": {
                          "type": "integer"
                        },
                        "inapp_name": {
                          "type": "null"
                        },
                        "inapp_base_name": {
                          "type": "null"
                        },
                        "currency": {
                          "type": "string"
                        },
                        "discount_percent": {
                          "type": "null"
                        },
                        "cost_with_bonus": {
                          "type": "number"
                        },
                        "bonus_money": {
                          "type": "number"
                        },
                        "account_money": {
                          "type": "number"
                        },
                        "can_be_paid_by_account_money": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "final_price",
                        "inapp_price",
                        "inapp_base_price",
                        "full_price",
                        "discount_price",
                        "litcoin_count",
                        "inapp_name",
                        "inapp_base_name",
                        "currency",
                        "discount_percent",
                        "cost_with_bonus",
                        "bonus_money",
                        "account_money",
                        "can_be_paid_by_account_money"
                      ]
                    },
                    "is_auto_speech_gift": {
                      "type": "boolean"
                    },
                    "subtitle": {
                      "type": "string"
                    },
                    "min_age": {
                      "type": "integer"
                    },
                    "is_adult_content": {
                      "type": "boolean"
                    },
                    "cover_height": {
                      "type": "integer"
                    },
                    "cover_width": {
                      "type": "integer"
                    },
                    "foreign_publisher_id": {
                      "type": "null"
                    },
                    "language_code": {
                      "type": "string"
                    },
                    "symbols_count": {
                      "type": "integer"
                    },
                    "expected_symbols_count": {
                      "type": "null"
                    },
                    "podcast_serial_number": {
                      "type": "null"
                    },
                    "last_updated_at": {
                      "type": "string"
                    },
                    "last_released_at": {
                      "type": "string"
                    },
                    "read_percent": {
                      "type": "integer"
                    },
                    "is_finished": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_promo": {
                      "type": "boolean"
                    },
                    "advertising_marking": {
                      "type": "null"
                    },
                    "event_data": {
                      "type": "null"
                    },
                    "my_art_status": {
                      "type": "integer"
                    },
                    "is_subscription_art": {
                      "type": "boolean"
                    },
                    "is_available_with_subscription": {
                      "type": "boolean"
                    },
                    "is_available_with_litres_subscription": {
                      "type": "boolean"
                    },
                    "availability_with_partner_subscriptions": {
                      "type": "array",
                      "items": {}
                    },
                    "art_subscription_status_for_user": {
                      "type": "string"
                    },
                    "is_abonement_art": {
                      "type": "boolean"
                    },
                    "is_available_with_abonement": {
                      "type": "boolean"
                    },
                    "can_be_preordered": {
                      "type": "boolean"
                    },
                    "is_preorder_notified_for_user": {
                      "type": "boolean"
                    },
                    "is_exclusive_abonement": {
                      "type": "boolean"
                    },
                    "is_drm": {
                      "type": "boolean"
                    },
                    "in_gifts": {
                      "type": "integer"
                    },
                    "is_fourth_art_gift": {
                      "type": "boolean"
                    },
                    "podcast_left_to_buy": {
                      "type": "null"
                    },
                    "availability": {
                      "type": "integer"
                    },
                    "available_from": {
                      "type": "string"
                    },
                    "library_information": {
                      "type": "null"
                    },
                    "persons": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "uuid": {
                              "type": "string"
                            },
                            "full_name": {
                              "type": "string"
                            },
                            "full_rodit": {
                              "type": "string"
                            },
                            "url": {
                              "type": "string"
                            },
                            "role": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "uuid",
                            "full_name",
                            "full_rodit",
                            "url",
                            "role"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "uuid": {
                              "type": "string"
                            },
                            "full_name": {
                              "type": "string"
                            },
                            "full_rodit": {
                              "type": "string"
                            },
                            "url": {
                              "type": "string"
                            },
                            "role": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "uuid",
                            "full_name",
                            "full_rodit",
                            "url",
                            "role"
                          ]
                        }
                      ]
                    },
                    "is_liked": {
                      "type": "boolean"
                    },
                    "rating": {
                      "type": "object",
                      "properties": {
                        "user_rating": {
                          "type": "null"
                        },
                        "rated_1_count": {
                          "type": "integer"
                        },
                        "rated_2_count": {
                          "type": "integer"
                        },
                        "rated_3_count": {
                          "type": "integer"
                        },
                        "rated_4_count": {
                          "type": "integer"
                        },
                        "rated_5_count": {
                          "type": "integer"
                        },
                        "rated_avg": {
                          "type": "number"
                        },
                        "rated_total_count": {
                          "type": "integer"
                        }
                      },
                      "required": [
                        "user_rating",
                        "rated_1_count",
                        "rated_2_count",
                        "rated_3_count",
                        "rated_4_count",
                        "rated_5_count",
                        "rated_avg",
                        "rated_total_count"
                      ]
                    },
                    "linked_arts": {
                      "type": "array",
                      "items": {}
                    },
                    "series": {
                      "type": "array",
                      "items": {}
                    },
                    "date_written_at": {
                      "type": "string"
                    },
                    "release_file_id": {
                      "type": "integer"
                    },
                    "preview_file_id": {
                      "type": "null"
                    },
                    "labels": {
                      "type": "object",
                      "properties": {
                        "is_bestseller": {
                          "type": "boolean"
                        },
                        "is_litres_exclusive": {
                          "type": "boolean"
                        },
                        "is_new": {
                          "type": "boolean"
                        },
                        "is_sales_hit": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "is_bestseller",
                        "is_litres_exclusive",
                        "is_new",
                        "is_sales_hit"
                      ]
                    },
                    "in_folders": {
                      "type": "null"
                    },
                    "is_archived": {
                      "type": "boolean"
                    },
                    "interacted_at": {
                      "type": "null"
                    },
                    "read_at": {
                      "type": "null"
                    },
                    "purchased_at": {
                      "type": "null"
                    },
                    "is_hidden": {
                      "type": "boolean"
                    },
                    "synchronized_arts": {
                      "type": "array",
                      "items": {}
                    },
                    "synchronizations": {
                      "type": "array",
                      "items": {}
                    },
                    "alternative_version": {
                      "type": "null"
                    },
                    "in_user_cart_status": {
                      "type": "string"
                    },
                    "is_draft_full_free": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "id",
                    "uuid",
                    "cover_url",
                    "url",
                    "title",
                    "cover_ratio",
                    "is_draft",
                    "art_type",
                    "prices",
                    "is_auto_speech_gift",
                    "subtitle",
                    "min_age",
                    "is_adult_content",
                    "cover_height",
                    "cover_width",
                    "foreign_publisher_id",
                    "language_code",
                    "symbols_count",
                    "expected_symbols_count",
                    "podcast_serial_number",
                    "last_updated_at",
                    "last_released_at",
                    "read_percent",
                    "is_finished",
                    "is_free",
                    "is_promo",
                    "advertising_marking",
                    "event_data",
                    "my_art_status",
                    "is_subscription_art",
                    "is_available_with_subscription",
                    "is_available_with_litres_subscription",
                    "availability_with_partner_subscriptions",
                    "art_subscription_status_for_user",
                    "is_abonement_art",
                    "is_available_with_abonement",
                    "can_be_preordered",
                    "is_preorder_notified_for_user",
                    "is_exclusive_abonement",
                    "is_drm",
                    "in_gifts",
                    "is_fourth_art_gift",
                    "podcast_left_to_buy",
                    "availability",
                    "available_from",
                    "library_information",
                    "persons",
                    "is_liked",
                    "rating",
                    "linked_arts",
                    "series",
                    "date_written_at",
                    "release_file_id",
                    "preview_file_id",
                    "labels",
                    "in_folders",
                    "is_archived",
                    "interacted_at",
                    "read_at",
                    "purchased_at",
                    "is_hidden",
                    "synchronized_arts",
                    "synchronizations",
                    "alternative_version",
                    "in_user_cart_status",
                    "is_draft_full_free"
                  ]
                }
              },
              "required": [
                "type",
                "instance"
              ]
            },
            {
              "type": "object",
              "properties": {
                "type": {
                  "type": "string"
                },
                "instance": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer"
                    },
                    "uuid": {
                      "type": "string"
                    },
                    "cover_url": {
                      "type": "string"
                    },
                    "url": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "cover_ratio": {
                      "type": "number"
                    },
                    "is_draft": {
                      "type": "boolean"
                    },
                    "art_type": {
                      "type": "integer"
                    },
                    "prices": {
                      "type": "object",
                      "properties": {
                        "final_price": {
                          "type": "number"
                        },
                        "inapp_price": {
                          "type": "null"
                        },
                        "inapp_base_price": {
                          "type": "null"
                        },
                        "full_price": {
                          "type": "number"
                        },
                        "discount_price": {
                          "type": "null"
                        },
                        "litcoin_count": {
                          "type": "integer"
                        },
                        "inapp_name": {
                          "type": "null"
                        },
                        "inapp_base_name": {
                          "type": "null"
                        },
                        "currency": {
                          "type": "string"
                        },
                        "discount_percent": {
                          "type": "null"
                        },
                        "cost_with_bonus": {
                          "type": "number"
                        },
                        "bonus_money": {
                          "type": "number"
                        },
                        "account_money": {
                          "type": "number"
                        },
                        "can_be_paid_by_account_money": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "final_price",
                        "inapp_price",
                        "inapp_base_price",
                        "full_price",
                        "discount_price",
                        "litcoin_count",
                        "inapp_name",
                        "inapp_base_name",
                        "currency",
                        "discount_percent",
                        "cost_with_bonus",
                        "bonus_money",
                        "account_money",
                        "can_be_paid_by_account_money"
                      ]
                    },
                    "is_auto_speech_gift": {
                      "type": "boolean"
                    },
                    "subtitle": {
                      "type": "string"
                    },
                    "min_age": {
                      "type": "integer"
                    },
                    "is_adult_content": {
                      "type": "boolean"
                    },
                    "cover_height": {
                      "type": "integer"
                    },
                    "cover_width": {
                      "type": "integer"
                    },
                    "foreign_publisher_id": {
                      "type": "null"
                    },
                    "language_code": {
                      "type": "string"
                    },
                    "symbols_count": {
                      "type": "integer"
                    },
                    "expected_symbols_count": {
                      "type": "null"
                    },
                    "podcast_serial_number": {
                      "type": "null"
                    },
                    "last_updated_at": {
                      "type": "string"
                    },
                    "last_released_at": {
                      "type": "string"
                    },
                    "read_percent": {
                      "type": "integer"
                    },
                    "is_finished": {
                      "type": "boolean"
                    },
                    "is_free": {
                      "type": "boolean"
                    },
                    "is_promo": {
                      "type": "boolean"
                    },
                    "advertising_marking": {
                      "type": "null"
                    },
                    "event_data": {
                      "type": "null"
                    },
                    "my_art_status": {
                      "type": "integer"
                    },
                    "is_subscription_art": {
                      "type": "boolean"
                    },
                    "is_available_with_subscription": {
                      "type": "boolean"
                    },
                    "is_available_with_litres_subscription": {
                      "type": "boolean"
                    },
                    "availability_with_partner_subscriptions": {
                      "type": "array",
                      "items": {}
                    },
                    "art_subscription_status_for_user": {
                      "type": "string"
                    },
                    "is_abonement_art": {
                      "type": "boolean"
                    },
                    "is_available_with_abonement": {
                      "type": "boolean"
                    },
                    "can_be_preordered": {
                      "type": "boolean"
                    },
                    "is_preorder_notified_for_user": {
                      "type": "boolean"
                    },
                    "is_exclusive_abonement": {
                      "type": "boolean"
                    },
                    "is_drm": {
                      "type": "boolean"
                    },
                    "in_gifts": {
                      "type": "integer"
                    },
                    "is_fourth_art_gift": {
                      "type": "boolean"
                    },
                    "podcast_left_to_buy": {
                      "type": "null"
                    },
                    "availability": {
                      "type": "integer"
                    },
                    "available_from": {
                      "type": "string"
                    },
                    "library_information": {
                      "type": "null"
                    },
                    "persons": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "uuid": {
                              "type": "string"
                            },
                            "full_name": {
                              "type": "string"
                            },
                            "full_rodit": {
                              "type": "string"
                            },
                            "url": {
                              "type": "string"
                            },
                            "role": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "uuid",
                            "full_name",
                            "full_rodit",
                            "url",
                            "role"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer"
                            },
                            "uuid": {
                              "type": "string"
                            },
                            "full_name": {
                              "type": "string"
                            },
                            "full_rodit": {
                              "type": "string"
                            },
                            "url": {
                              "type": "string"
                            },
                            "role": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "uuid",
                            "full_name",
                            "full_rodit",
                            "url",
                            "role"
                          ]
                        }
                      ]
                    },
                    "is_liked": {
                      "type": "boolean"
                    },
                    "rating": {
                      "type": "object",
                      "properties": {
                        "user_rating": {
                          "type": "null"
                        },
                        "rated_1_count": {
                          "type": "integer"
                        },
                        "rated_2_count": {
                          "type": "integer"
                        },
                        "rated_3_count": {
                          "type": "integer"
                        },
                        "rated_4_count": {
                          "type": "integer"
                        },
                        "rated_5_count": {
                          "type": "integer"
                        },
                        "rated_avg": {
                          "type": "number"
                        },
                        "rated_total_count": {
                          "type": "integer"
                        }
                      },
                      "required": [
                        "user_rating",
                        "rated_1_count",
                        "rated_2_count",
                        "rated_3_count",
                        "rated_4_count",
                        "rated_5_count",
                        "rated_avg",
                        "rated_total_count"
                      ]
                    },
                    "linked_arts": {
                      "type": "array",
                      "items": {}
                    },
                    "series": {
                      "type": "array",
                      "items": {}
                    },
                    "date_written_at": {
                      "type": "string"
                    },
                    "release_file_id": {
                      "type": "integer"
                    },
                    "preview_file_id": {
                      "type": "null"
                    },
                    "labels": {
                      "type": "object",
                      "properties": {
                        "is_bestseller": {
                          "type": "boolean"
                        },
                        "is_litres_exclusive": {
                          "type": "boolean"
                        },
                        "is_new": {
                          "type": "boolean"
                        },
                        "is_sales_hit": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "is_bestseller",
                        "is_litres_exclusive",
                        "is_new",
                        "is_sales_hit"
                      ]
                    },
                    "in_folders": {
                      "type": "null"
                    },
                    "is_archived": {
                      "type": "boolean"
                    },
                    "interacted_at": {
                      "type": "null"
                    },
                    "read_at": {
                      "type": "null"
                    },
                    "purchased_at": {
                      "type": "null"
                    },
                    "is_hidden": {
                      "type": "boolean"
                    },
                    "synchronized_arts": {
                      "type": "array",
                      "items": {}
                    },
                    "synchronizations": {
                      "type": "array",
                      "items": {}
                    },
                    "alternative_version": {
                      "type": "null"
                    },
                    "in_user_cart_status": {
                      "type": "string"
                    },
                    "is_draft_full_free": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "id",
                    "uuid",
                    "cover_url",
                    "url",
                    "title",
                    "cover_ratio",
                    "is_draft",
                    "art_type",
                    "prices",
                    "is_auto_speech_gift",
                    "subtitle",
                    "min_age",
                    "is_adult_content",
                    "cover_height",
                    "cover_width",
                    "foreign_publisher_id",
                    "language_code",
                    "symbols_count",
                    "expected_symbols_count",
                    "podcast_serial_number",
                    "last_updated_at",
                    "last_released_at",
                    "read_percent",
                    "is_finished",
                    "is_free",
                    "is_promo",
                    "advertising_marking",
                    "event_data",
                    "my_art_status",
                    "is_subscription_art",
                    "is_available_with_subscription",
                    "is_available_with_litres_subscription",
                    "availability_with_partner_subscriptions",
                    "art_subscription_status_for_user",
                    "is_abonement_art",
                    "is_available_with_abonement",
                    "can_be_preordered",
                    "is_preorder_notified_for_user",
                    "is_exclusive_abonement",
                    "is_drm",
                    "in_gifts",
                    "is_fourth_art_gift",
                    "podcast_left_to_buy",
                    "availability",
                    "available_from",
                    "library_information",
                    "persons",
                    "is_liked",
                    "rating",
                    "linked_arts",
                    "series",
                    "date_written_at",
                    "release_file_id",
                    "preview_file_id",
                    "labels",
                    "in_folders",
                    "is_archived",
                    "interacted_at",
                    "read_at",
                    "purchased_at",
                    "is_hidden",
                    "synchronized_arts",
                    "synchronizations",
                    "alternative_version",
                    "in_user_cart_status",
                    "is_draft_full_free"
                  ]
                }
              },
              "required": [
                "type",
                "instance"
              ]
            }
          ]
        },
        "extra": {
          "type": "object",
          "properties": {
            "counters": {
              "type": "object",
              "properties": {
                "all": {
                  "type": "integer"
                },
                "text_book": {
                  "type": "integer"
                },
                "audiobook": {
                  "type": "integer"
                },
                "person": {
                  "type": "integer"
                },
                "collection": {
                  "type": "integer"
                },
                "series": {
                  "type": "integer"
                },
                "genre": {
                  "type": "integer"
                },
                "tag": {
                  "type": "integer"
                },
                "podcast_episode": {
                  "type": "integer"
                },
                "podcast": {
                  "type": "integer"
                },
                "publisher": {
                  "type": "integer"
                },
                "books_filtered_by_libraries": {
                  "type": "integer"
                }
              },
              "required": [
                "all",
                "text_book",
                "audiobook",
                "person",
                "collection",
                "series",
                "genre",
                "tag",
                "podcast_episode",
                "podcast",
                "publisher",
                "books_filtered_by_libraries"
              ]
            },
            "pagination": {
              "type": "object",
              "properties": {
                "next_offset": {
                  "type": "null"
                }
              },
              "required": [
                "next_offset"
              ]
            },
            "applied_correction": {
              "type": "null"
            }
          },
          "required": [
            "counters",
            "pagination",
            "applied_correction"
          ]
        },
        "facets": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "type": {
                  "type": "string"
                },
                "title": {
                  "type": "string"
                },
                "data": {
                  "type": "array",
                  "items": [
                    {
                      "type": "object",
                      "properties": {
                        "value": {
                          "type": "string"
                        },
                        "documents_count": {
                          "type": "integer"
                        },
                        "is_selected": {
                          "type": "boolean"
                        },
                        "title": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "value",
                        "documents_count",
                        "is_selected",
                        "title"
                      ]
                    }
                  ]
                },
                "subtitle": {
                  "type": "null"
                },
                "help_text": {
                  "type": "string"
                }
              },
              "required": [
                "name",
                "type",
                "title",
                "data",
                "subtitle",
                "help_text"
              ]
            },
            {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "type": {
                  "type": "string"
                },
                "title": {
                  "type": "string"
                },
                "data": {
                  "type": "array",
                  "items": [
                    {
                      "type": "object",
                      "properties": {
                        "value": {
                          "type": "string"
                        },
                        "documents_count": {
                          "type": "integer"
                        },
                        "is_selected": {
                          "type": "boolean"
                        },
                        "title": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "value",
                        "documents_count",
                        "is_selected",
                        "title"
                      ]
                    }
                  ]
                },
                "subtitle": {
                  "type": "null"
                },
                "help_text": {
                  "type": "string"
                }
              },
              "required": [
                "name",
                "type",
                "title",
                "data",
                "subtitle",
                "help_text"
              ]
            },
            {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "type": {
                  "type": "string"
                },
                "title": {
                  "type": "string"
                },
                "data": {
                  "type": "array",
                  "items": [
                    {
                      "type": "object",
                      "properties": {
                        "value": {
                          "type": "string"
                        },
                        "documents_count": {
                          "type": "integer"
                        },
                        "is_selected": {
                          "type": "boolean"
                        },
                        "title": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "value",
                        "documents_count",
                        "is_selected",
                        "title"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "value": {
                          "type": "string"
                        },
                        "documents_count": {
                          "type": "integer"
                        },
                        "is_selected": {
                          "type": "boolean"
                        },
                        "title": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "value",
                        "documents_count",
                        "is_selected",
                        "title"
                      ]
                    }
                  ]
                },
                "subtitle": {
                  "type": "null"
                },
                "help_text": {
                  "type": "null"
                }
              },
              "required": [
                "name",
                "type",
                "title",
                "data",
                "subtitle",
                "help_text"
              ]
            },
            {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "type": {
                  "type": "string"
                },
                "title": {
                  "type": "string"
                },
                "data": {
                  "type": "array",
                  "items": [
                    {
                      "type": "object",
                      "properties": {
                        "value": {
                          "type": "string"
                        },
                        "documents_count": {
                          "type": "integer"
                        },
                        "is_selected": {
                          "type": "boolean"
                        },
                        "title": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "value",
                        "documents_count",
                        "is_selected",
                        "title"
                      ]
                    }
                  ]
                },
                "subtitle": {
                  "type": "null"
                },
                "help_text": {
                  "type": "null"
                }
              },
              "required": [
                "name",
                "type",
                "title",
                "data",
                "subtitle",
                "help_text"
              ]
            },
            {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "type": {
                  "type": "string"
                },
                "title": {
                  "type": "string"
                },
                "data": {
                  "type": "array",
                  "items": [
                    {
                      "type": "object",
                      "properties": {
                        "value": {
                          "type": "string"
                        },
                        "documents_count": {
                          "type": "integer"
                        },
                        "is_selected": {
                          "type": "boolean"
                        },
                        "title": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "value",
                        "documents_count",
                        "is_selected",
                        "title"
                      ]
                    }
                  ]
                },
                "subtitle": {
                  "type": "string"
                },
                "help_text": {
                  "type": "null"
                }
              },
              "required": [
                "name",
                "type",
                "title",
                "data",
                "subtitle",
                "help_text"
              ]
            }
          ]
        },
        "fast_facets": {
          "type": "array",
          "items": {}
        }
      },
      "required": [
        "data",
        "extra",
        "facets",
        "fast_facets"
      ]
    }
  },
  "required": [
    "status",
    "error",
    "payload"
  ]
}