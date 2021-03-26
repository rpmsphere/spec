Name:           gwhois
Version:        20100728
Release:        3.1
License:        GPL
Group:          Productivity/Networking/Other
Requires:       curl perl-libwww-perl
Requires:       xinetd
Requires:       lynx
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
URL:            http://gwhois.de/
Source0:        http://gwhois.de/gwhois/gwhois_%{version}.tar.gz
Source1:        %{name}.xinetd
Summary:        Universal Whois Client/Server suitable for all TLDs and IPs

%description
gwhois is a generic whois client (and server) which strives to know the right
server to query for each and every top level domain and IP address. You can ask
gwhois about a domain or IP address, and it will automatically forward your
query to the appropriate server. It even queries whois servers that can only be
reached by a Web form, and outputs the results as text. It can be used as a
client or as a relaying server, so you can use your normal whois client to ask
gwhois.

Authors:
--------
    Michael Holzt <kju@debian.org>

%prep
%setup -n %{name}-%{version}

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -D -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
%{__install} -D -m 0644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
%{__install} -D -m 0644 pattern $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/pattern
%{__install} -D -m 0644 %{S:1} $RPM_BUILD_ROOT%{_sysconfdir}/xinetd.d/%{name}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/xinetd.d/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%doc NEWS.Debian README.RIPE TODO INSTALL debian/changelog

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 20100728
- Rebuild for Fedora
* Tue Apr 19 2011 mrueckert@suse.de
- update to 20100728
  * add "last update of whois database" line to output from verisign-grs
  * updated/fixed ipv4 netblock lists
- additional changes from 20100727
  * 2a00:: is ripe, also fixed ipv6 pattern in whole (closes: Bug#585072)
  * fixed ARIN lookups
- additional changes from 20100515
  * Removed charset parameter from DENIC queries, convert parameter
    charset, use libidn for punycode encoding of queried multilingual
    domains (closes: Bug#567834)
  * Applied manpage fixes (closes: Bug#551758)
- additional changes from 20090717.1
  * Added .tel whois (closes: Bug#524675)
- additional changes from 20081019
  * Throw error on empty query string.
- additional changes from 20080925
  * Changed .by URL, same unhelpful output as before (closes: Bug#500042)
- additional changes from 20080716
  * Verbose output for .name, tnx John McGowan
- additional changes from 20080626
  * Fixed .ms, tnx Uwe Sinha (closes: Bug#488093)
- additional changes from 20080219
  * Added SIXXS-handles, tnx Christian Seitz (closes: Bug#458470)
  * Modified/Fixed .af, .ai, .an, .az, .bi, .cf, .ci, .cl, .dk, .ec, .eg, .fj,
    .gd, .ge, .gi, .gm, .gn, .gp, .gs, .gy, .hn, .hr, .ir, .ki, .kz, .la, .lc,
    .lk, .ly, .ma, .mc, .mg, .mm, .mn, .mr, .ms, .mt, .mu, .nc, .nf, .pl, .pm,
    .pw, .py, .sc, .sd, .sm, .sn, .sr, .sv, .tc, .tg, .tl, .tm, .uy, .uz, .vc,
    .ve, .vn, .ws, .jobs, .mil, .travel
  * Added .arpa, .asia (yet defunct), .tel (no whois) and Subdomain-Whois
    of Centralnic for certain subdomains under .com., .net and .org (e.g.
    gb.net).
  * Removed .cs
- additional changes from 20071030
  * Fixed .im (closes: Bug#448661)
- additional changes from 20070926
  * Added .me (closes: Bug#444198), added .kp, changed .rs
* Wed Sep  5 2007 mrueckert@suse.de
- update to 20070905
  * TLD .va is now included in the ripe database, tnx Mark Thomas
  * included portuguese translation, tnx Americo Monteiro
    (closes: Bug#435729)
  * included spanish translation, tnx Rudy Godoy Guillen
    (closes: Bug#426174)
  * made output from verisign-grs more verbose
* Thu Aug 23 2007 mrueckert@suse.de
- update to 20070822
  * Fixed .de (AGAIN due to a subtile change of the whois service)
* Sun Apr  8 2007 mrueckert@suse.de
- update to 20070403
  * Fixed .de
  * Fixed/Updated .as
* Sun Mar  4 2007 mrueckert@suse.de
- update to 20070218:
  * Fixed .co and .pk
  * Handles ending on '-ap' are APNIC (closes: Bug#411248)
  * 116/6, 120/8 new to APNIC
  * added redirect modifier feature (see readme.ripe)
    (closed: Bug#404622)
  * Added lookup for four byte AS numbers (e.g. AS3.1)
    (closes: Bug#406070)
  * Broadened regex for lim- (RIPE), added poem- (RIPE)
    (closes: Bug#401542)
  * Added a new query method 'multiple' for doing multiple lookups
    for one query. This is used for .vg which provides
    complementing data via CGI _and_ via WHOIS.
  * Also fixed CGI-URL for .vg, tnx VT100 (closes: Bug#401339)
* Fri Nov 10 2006 mrueckert@suse.de
- update to 20061113:
  * Fixed .info, tnx Stefan Schmidt (closes: Debian Bug#397899)
* Mon Oct  9 2006 mrueckert@suse.de
- update to 20061002:
  * .mobi now has a whois server
  * Changed README.upgrade into NEWS.Debian
  * 196/8 now complete Afrinoc (tnx MarcL)
  * 77/8, 78/8, 79/8 RIPE (new)
  * 201/8, 189/8, 190/8 LACNIC (not new, shame on me)
  * Fixed 122/6 -> 122/7, 124/7
* Thu Apr 27 2006 mrueckert@suse.de
- update to 20060419:
  * The "i-should-have-done-this-much-earlier" Release. Sorry folks.
  * Added .eu (closes: Debian Bug#351793)
  * Fixed .il (closes: Debian Bug#355039)
  * Added extensive list of ip networks transfered to AFRINIC,
    many tnx to Axel Rau
  * Added .cat, .mobi
  * Added 89/8, 90/8, 91/8 to RIPE
  * Added 58/7, 121/8, 122/6, 126/8, 169.208/12, 196.192/13 to APNIC
  * Added swedish translation. Thanks Daniel Nylander.
    (closes: Debian Bug#339762)
* Mon Sep 26 2005 mrueckert@suse.de
- Update to 20050925
