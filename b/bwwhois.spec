Name:			bwwhois
Version:		5.0
Release:		10.1
License:		Artistic License
URL:			https://whois.bw.org/
Summary:		Bill Weinman replacement Whois client
Group:			Productivity/Networking/Diagnostic
Source:			%{name}-%{version}.tar.gz
Requires:		perl
Requires:		perl(DBD::mysql)
BuildRequires:		perl(DBD::mysql)
Provides:		whois

%define _wwwdir 	/var/www/htdocs
%define _cgibin		/var/www/cgi-bin
%define _confdir	/etc


%description
The whois system changed when the ICANN cabal assumed control of the domain
registration system on 1 December 1999. The whois clients in use at that
time stopped working when the new system was deployed. That's why I wrote
this one.

Over time BW Whois evolved into the most full-featured whois client available
providing features like a self-detecting CGI mode and SQL database caching,
for those who need such features, while still maintaining a simple command-line
interface for those who just need that.

%prep
%setup -q

%install
%{__rm} -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m755 whois $RPM_BUILD_ROOT/%{_bindir}/whois

mkdir -p $RPM_BUILD_ROOT/etc/whois
install -m644 sd.conf $RPM_BUILD_ROOT/etc/whois/sd.conf
install -m644 tld.conf $RPM_BUILD_ROOT/etc/whois/tld.conf
install -m644 whois.conf $RPM_BUILD_ROOT/etc/whois/whois.conf

mkdir -p $RPM_BUILD_ROOT/%{_cgibin}
install -m755 whois $RPM_BUILD_ROOT/%{_cgibin}/whois.cgi

mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
install -m644 whois.1 $RPM_BUILD_ROOT/%{_mandir}/man1/whois.1

mkdir -p $RPM_BUILD_ROOT/%{_wwwdir}
install -m644 whois.html $RPM_BUILD_ROOT/%{_wwwdir}/whois.html
install -m644 whois-first.html $RPM_BUILD_ROOT/%{_wwwdir}/whois-first.html
install -m644 whois-notfound.html $RPM_BUILD_ROOT/%{_wwwdir}/whois-notfound.html
install -m644 whois-error-403.html $RPM_BUILD_ROOT/%{_wwwdir}/whois-error-403.html
install -m644 whois-error-408.html $RPM_BUILD_ROOT/%{_wwwdir}/whois-error-408.html

mkdir -p $RPM_BUILD_ROOT/%{perl_archlib}
install -m755 bwInclude.pm $RPM_BUILD_ROOT/%{perl_archlib}/bwInclude.pm

%files
%{_bindir}/whois
%{_cgibin}/whois.cgi
%{perl_archlib}/bwInclude.pm
%dir %{_confdir}/whois
%config(noreplace) /etc/whois/sd.conf
%config(noreplace) /etc/whois/tld.conf
%config(noreplace) /etc/whois/whois.conf
%{_mandir}/man1/whois.*
%{_wwwdir}/whois-error-403.html
%{_wwwdir}/whois-error-408.html
%{_wwwdir}/whois-first.html
%{_wwwdir}/whois.html
%{_wwwdir}/whois-notfound.html
%doc create_whois.sql COPYRIGHT DISCLAIMER HISTORY INSTALL README whois.txt

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 5.0
- Rebuilt for Fedora
