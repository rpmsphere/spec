Name:    leocad-data
Version: 11494
Release: 1
Summary: Data files for LeoCAD: bricks, textures and font
Summary(ru_RU): Файлы для %progname: описание блоков, текстуры и шрифт
License: Distributable
URL:     http://www.leocad.org
Source:  Library-Linux-%{version}.zip
Group:   Games/Puzzles
BuildArch: noarch

%description
Pieces, textures and font for LeoCAD.

%description -l ru_RU
Описание блоков, текстуры и шрифт для LeoCAD.

%prep
%setup -q -c

%build

%install
mkdir -p %buildroot%_datadir/leocad
install * %buildroot%_datadir/leocad

%files
%_datadir/leocad/*

%changelog
* Wed Sep 11 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 11494
- Rebuild for Fedora
* Mon Sep 27 2010 Igor Vlasenko <viy@altlinux.ru> 0.75.20100922-alt1
- updated to pieces-3934.zip (2010-09-22)
* Mon May 25 2009 Fr. Br. George <george@altlinux.ru> 0.75.20090503-alt1
- Fresh unversioned files
* Sun Oct 07 2007 Fr. Br. George <george@altlinux.ru> 0.75-alt1
- Initial build for ALT
