Name: pasang-emas
Summary: A traditional board game of Brunei
Version: 6.3.0
Release: 1
Group: Amusements/Games
License: GPLv3
URL: https://pasang-emas.sourceforge.net/
Source0: https://sourceforge.net/projects/pasang-emas/files/pasang-emas/%{version}/%{name}-%{version}.tar.xz
BuildRequires: gtk3-devel
BuildRequires: intltool
BuildRequires: gnome-doc-utils
BuildRequires: python3

%description
Pasang is a traditional two-player board game of Brunei. The game starts with
a board-full of tokens. The players take turn capturing these tokens.
The player with the most tokens wins.

%prep
%setup -q

%build
%configure --disable-scrollkeeper
make %{?_smp_mflags}

%install
%make_install
sed -i 's|^Name=.*|Name=Pasang Emas|' %{buildroot}%{_datadir}/applications/%{name}.desktop
mv %{buildroot}%{_datadir}/icons %{buildroot}%{_datadir}/pixmaps

%files
%doc AUTHORS NEWS ChangeLog COPYING README
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
#{_datadir}/gnome/help/%{name}
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
#{_datadir}/omf/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}*.png
%{_datadir}/help/*/pasang-emas
%{_datadir}/metainfo/bn.pasang.pasang-emas.appdata.xml

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 6.3.0
- Rebuilt for Fedora
