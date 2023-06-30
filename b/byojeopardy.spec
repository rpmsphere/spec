Name: byojeopardy
Group: Games
Version: 1.2.14
Release: 4.1
License: GPL2
URL: https://www.wolfescience.com/byojeopardy/
Summary: Creates your own jeopardy games
Source: %{name}-%{version}.tar.gz
BuildRequires: libpng-devel
BuildRequires: autoconf
BuildRequires: libxslt-devel libxml2-devel gtk2-devel
Requires:      gtk2

%description
Build Your Own Jeopardy (BYOJeopardy) helps you make custom game boards
that you can use in the classroom or play with friends.

%prep
%setup -q
sed -i 's|attribute, NULL|fontfamily, NULL|' xhtmlite/xhtmlite_module/xhtmlbuffer.c

%build
LDFLAGS=-Wl,--allow-multiple-definition
touch po/POTFILES.in
touch po/Makefile.in.in
%configure
make 

%install
make DESTDIR=$RPM_BUILD_ROOT install
sed -i 's|Icon=|Icon=%{_datadir}/%{name}/pixmaps/|' $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}

%changelog
* Thu Jun 07 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.14
- Rebuilt for Fedora
* Thu May 17 2012 Christian Schneemann
- Initial package
