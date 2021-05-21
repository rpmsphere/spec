Summary:	RIA links for oxlauncher
Name:		oxlauncher-RIAs
Version:	0.2
Release:	2
License:	MIT
Group:		Applications/Internet
Source:		%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	oxlauncher

%description
Links of various Rich Internet Application for oxlauncher.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/oxlauncher
install -m 644 *.png $RPM_BUILD_ROOT%{_datadir}/oxlauncher
install -d $RPM_BUILD_ROOT%{_datadir}/applications
install -m 644 *.desktop $RPM_BUILD_ROOT%{_datadir}/applications

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/oxlauncher/*.png
%{_datadir}/applications/*.desktop

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Fri Jan 28 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Initial package
