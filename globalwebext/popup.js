// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

jQuery.getJSON("http://192.168.1.217:8000/gw/get_countries",function(data){
		for (var i = 0; i <= 2;i++){
			$(document.createElement("img"))
				.attr({src:data[i].img_url,title:data[i].code})
				.appendTo(document.body)
				.click(function(){
						var country_url = "http://192.168.1.217:8000/gw/get_country?code=GR";
						jQuery.getJSON(country_url, function(data){
								var config = {
									mode: "fixed_servers",
									rules: {
										singleProxy: {
											scheme: "http",
											host: data.proxy_url,
											port:data.proxy_port
										},
									}
								};
								chrome.proxy.settings.set(
														  {value: config, scope: 'regular'},
														  function() {});
							});
					})
				}
	});
