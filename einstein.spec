Summary:	Remake of old DOS game Sherlock
Name:		einstein
Version:	2.0
Release:	20.4
License:	GPLv2+
Group:		Games/Puzzles
URL:		http://games.flowix.com/en/index.html
Source:		http://www.babichev.info/files/einstein/%{name}-%{version}-src.tar.gz
Source1:	%{name}-1.0-html-pages.tgz
Source2:	%{name}-wrapper
Source3:	icon.bmp
Source4:	einstein.desktop
Source5:	einstein.png
Patch1:		einstein-math_h.patch
Patch2:		einstein-Makefile.patch
Patch3:		einstein-formatter_cpp.patch
Patch4:		einstein-2.0-deb-icon_change.patch
Patch5:		einstein-2.0-deb-font_change.patch
Patch6:		einstein-2.0-deb-random_init.patch
Patch7:		einstein-2.0-alt-rules_clarification.patch
Patch8:		einstein-2.0-alt-fix_mkres_link.patch
Patch9:		einstein-2.0-alt-translation_fix.patch
Patch10:	einstein-2.0-gcc43.patch
Patch11:	einstein-2.0-no-strip.patch
BuildRequires:	dejavu-sans-fonts
BuildRequires:	makedepend
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	pkgconfig(zlib)

%description
Einstein puzzle is cross-platform open source remake of old DOS game Sherlock
which was inspired by Albert Einstein's puzzle. Einstein said that only those
with an intelligence quotient of 97 percentile and higher should be able to
solve it.

The game goal is to open all cards in square of 6x6 cards.
Every row of square contains cards of one type only. For example, first row
contains arabic digits, second - letters, third - rome digits, fouths - dices,
fifth - geometric figures, sixs - mathematic symbols.

%files
%doc doc/*
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png

%prep
%setup
%setup -q -T -D -a 1

%patch1
%patch2
%patch3 -p2
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
install %{SOURCE3} res/
mv %{name} doc
cp /usr/share/fonts/dejavu/DejaVuSans.ttf res/

%build
#make depend
make -C mkres OPTIMIZE="%{optflags}"
pushd res
../mkres/mkres --source resources.descr --output ../einstein.res
popd
make PREFIX=/usr OPTIMIZE="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}/res
%make_install PREFIX=%{buildroot}%{_prefix}
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}.bin
install %{SOURCE2} %{buildroot}%{_bindir}/%{name}
chmod 755 %{buildroot}%{_bindir}/%{name}
install -Dm 0644 %{SOURCE4} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm 0644 %{SOURCE5} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuild for Fedora
