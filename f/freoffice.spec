Name: freoffice
Summary: Simple Office file Viewer
Version: 0.3
Release: 1
License: GPLv2+
Group: Applications/Productivity
Source: http://repository.maemo.org/extras-devel/pool/fremantle/free/source/f/%{name}/%{name}_%{version}-1.tar.gz
URL: http://maemo.org/packages/view/freoffice/
BuildRequires: cmake, koffice-devel
Requires: koffice-kchart

%description
FreOffice is a mobile Office suite powered by KOffice. Users can view office
documents(Microsoft formats and ODF), carry basic editing and create new documents.

%prep
%setup -q

%build
%cmake .
%__make %{?_smp_mflags}

%install
%__rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/FreOffice
%{_datadir}/applications/hildon/FreOffice.desktop
%{_datadir}/dbus-1/services/com.nokia.FreOffice.service
%{_datadir}/freoffice-templates

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Fri May 06 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
