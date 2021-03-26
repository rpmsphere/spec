%define realname CardCol

Name:		cardcol		
Version:	0.9.51
Release:	1
Summary:	A collection of cardgames	
Group:		Amusements/Games
License:	GPL	
URL: 		http://cardcol.sourceforge.net		
Source0:	http://sourceforge.net/projects/cardcol/files/%{name}/%{realname}-%{version}/%{realname}-%{version}.tar.gz
Source1:	CardCol-0.9.51.zh_TW.po
BuildRequires:  libYGP-devel
BuildRequires:	gtkmm24-devel
BuildRequires:  cardpics
Requires: 	cardpics

%description
A collection of cardgames I (usually) learned from various people around
the world, usually while travelling (what could kill time better in >10 hour
bus/train/whatever rides than a good cardgame?).

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:       cardpics

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{realname}-%{version}
msgfmt %{SOURCE1} -o po/zh_TW.gmo 
sed -i 's/de en es tr/de en es tr zh_TW/' configure.ac
sed -i '211s|deck|back|' card/DeckSelect.cpp
sed -i 's|(CARDDECKS_DIR)|(CARDDECKS_DIR CARDDECKS_BACK)|' src/CardOptions.meta
sed -i 's|galeon|firefox|' src/Options.meta
sed -i 's|icons|pixmaps|' data/Makefile*
sed -i 's|Exec=CardCol|Exec=cardcol|' data/CardCol.desktop
sed -i '72s|return back_|return bool(back_)|' card/Images.h

%build
%configure	
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/usr/bin/bash
rm -f \$HOME/.Cardgames
exec %{realname}
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%attr(755,root,root) %{_bindir}/%{name}
%{_bindir}/%{realname}
%{_datadir}/locale/*/LC_MESSAGES/%{realname}.mo
%{_datadir}/doc/%{realname}
%{_datadir}/pixmaps/%{realname}.png
%{_datadir}/applications/%{realname}.desktop
%{_libdir}/libCard*.so

%files devel
%{_libdir}/libCard.*a
%{_includedir}/card

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.51
- Rebuild for Fedora
- Workaround for reading ini bug
* Thu Nov 15 2012 kevinchen <kevin.chen@ossii.com.tw> - 0.9.51-2
- Compiler debug & Package.
- Localized this Package in Traditional Chinese.
* Mon Jun 4 2012 johnwu <johnwu@ossii.com.tw>
- First
