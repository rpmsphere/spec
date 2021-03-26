Name: nitroshare
Summary: Simple utility for sharing files across a network
Version: 0.2
Release: 13.1
Group: Converted/net
License: see /usr/share/doc/nitroshare/copyright
URL: https://launchpad.net/nitroshare/
Source0: https://launchpad.net/nitroshare/0.2/0.2/+download/%{name}_%{version}.tar.gz
BuildRequires: gcc-c++, qt4-devel, qjson-devel
BuildRequires: qxmlrpc-devel

%description
NitroShare makes it easy to share files across a home network. Just install
the application on each machine you want to use for sharing files. Then simply
drag-and-drop files on to the share box or use the indicator menu to send
files.

%prep
%setup -q -n %{name}
sed -i -e 's|nitroshare.png|nitroshare|' -e 's|/opt/extras.ubuntu.com/nitroshare/||' resource/other/extras-%{name}.desktop

%build
qmake-qt4
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm644 nautilus/%{name}.py $RPM_BUILD_ROOT%{_datadir}/nautilus-python/extensions/%{name}.py
install -Dm644 other/%{name}.svg $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.svg
install -Dm644 resource/other/extras-%{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -Dm644 debian/%{name}.1 $RPM_BUILD_ROOT%{_datadir}/man/man1/%{name}.1

%files
%doc README LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/man/man1/%{name}.1.*
%{_datadir}/nautilus-python/extensions/%{name}.py*
%{_datadir}/pixmaps/%{name}.svg

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuild for Fedora

