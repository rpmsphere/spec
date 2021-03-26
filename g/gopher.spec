Summary:	A gopher client
Name:		gopher
Version:	3.0.13
Release:	2.1
License:	GPL
Group:		Applications/Networking
Vendor:		John Goerzen <jgoerzen@complete.org>
Source0:	http://gopher.quux.org:70/give-me-gopher/%{name}_%{version}.tar.gz
URL:		gopher://gopher.quux.org/1/Software/Gopher
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gopher client is used to talk to gopher servers.

%prep
%setup -q -n %{name}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man{1,5,8}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	MAN1DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	MAN5DIR=$RPM_BUILD_ROOT%{_mandir}/man5 \
	MAN8DIR=$RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc copyright README doc/{FAQ,PLATFORMS,TODO} doc/[cgo]*.changes
%doc announcements/*.html
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/gopher
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/gopher/gopher.hlp
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/gopher/gopher.rc
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/gopher/gopherremote.rc
%{_mandir}/man1/*
%{_mandir}/man5/gopherrc.5*

%changelog
* Fri Jun 15 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.13
- Rebuild for Fedora

* Sat Aug 28 2004 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log: gopher.spec,v $
Revision 1.6  2004/08/28 21:03:48  undefine
- update to 3.0.6, there is no gopherd anymore, use pygopherd

Revision 1.5  2003/07/23 09:35:40  qboosh
- more fixes in ac patch, some work in spec - builds now

Revision 1.4  2003/05/26 16:25:07  malekith
- massive attack: adding Source-md5

Revision 1.3  2003/05/25 05:48:21  misi3k
- massive attack s/pld.org.pl/pld-linux.org/

Revision 1.2  2003/02/28 10:07:56  trojan
- massive attack: perl -pi -e "s/^#+\%\{/#\%\%\{/"

Revision 1.1  2002/11/04 01:14:45  ankry
- initial release, NFY
