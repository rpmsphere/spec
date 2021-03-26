%define		upstream_name %{name}.x
%define		mpdm_ver 2.1.7
%define		mpsl_ver 2.2.2

Name:		mp-5
Version:	5.2.13
Release:	5.1
Summary:	Minimum-Profit Text Editor
Group:		Editors
License:	GPLv2
URL:		http://triptico.com/software/mp.html
Source0:	https://github.com/angelortega/mp-5.x/archive/%{version}/mp-%{version}.tar.gz
Source1:	https://github.com/angelortega/mpdm/archive/%{mpdm_ver}/mpdm-%{mpdm_ver}.tar.gz
Source2:	https://github.com/angelortega/mpsl/archive/%{mpsl_ver}/mpsl-%{mpsl_ver}.tar.gz
Patch0:		config.sh-qt5.patch
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	byacc
#BuildRequires:	mp_doccer
BuildRequires:	pcre-devel
BuildRequires:	qt5-devel
BuildRequires:	ncurses-devel
#BuildRequires:	grutatxt
BuildRequires:	glibc-devel

%description
A text editor for programmers including the following features:
- Fully scriptable using a C-like scripting language.
- Unlimited undo levels.
- Complete Unicode support.
- Multiple files can be edited at the same time and blocks copied and pasted
  among them.
- Syntax highlighting for many popular languages / file formats: C, C++, Perl,
  Shell Scripts, Ruby, Php, Python, HTML...
- Creative use of tags: tags created by the external utility ctags are used to
  move instantaneously to functions or variables inside your current source
  tree. Tags are visually highlighted (underlined), and symbol completion can
  be triggered to avoid typing your own function names over and over.
- Intelligent help system: pressing F1 over any word of a text being edited
  triggers the underlying system help (calling man when editing C or Shell
  files, perldoc with Perl, ri on Ruby...).
- Understandable interface: drop-down menus, reasonable default key bindings.
- Configurable keys, menus and colors.
- Text templates can be easily defined / accessed.
- Multiplatform: Console/curses, Qt4, KDE4, GTK+, MS Windows (both windowed
  and console).
- Automatic indentation, word wrapping, internal grep, learning / repeating
  functions.
- Spellchecking support (via the ispell package).
- Multilingual.
- Password-protected, encrypted text files (using the ARCFOUR algorithm).
- It helps you abandon vi, emacs and other six-legged freaks definitely.

%prep
%setup -q -a1 -a2 -n %{upstream_name}-%{version}
%autopatch -p1
mv mpsl-%{mpsl_ver} mpsl
mv mpdm-%{mpdm_ver} mpdm

%build
export CPP="g++ -std=gnu++11"
./config.sh \
	--prefix=%{_prefix} \
	--with-moc=%{_qt5_bindir}/moc \
	--withouot-qt4 \
	--without-gtk \
	--without-win32 \
	--with-pcre
%make_build

%install
%make_install
%find_lang minimum-profit
%__rm -rf %{buildroot}%{_datadir}/doc/%{name}

%files -f minimum-profit.lang
%license COPYING
%doc README RELEASE_NOTES AUTHORS *sample TODO* doc/*
%doc mpsl/README* mpsl/doc/*
%doc mpdm/doc/*
%{_bindir}/%{name}
%{_bindir}/mpsl
%{_datadir}/%{name}

%changelog
* Thu Jul 26 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 5.2.13
- Rebuild for Fedora
* Tue Feb 27 2018 kekepower <kekepower> 5.2.13-3.mga7
  (not released yet)
+ Revision: 1205559
- Enable Qt5
- Add patch for Qt5 detection, submitted upstream
- Add symlink to mp and mped
* Tue Feb 27 2018 kekepower <kekepower> 5.2.13-1.mga7
+ Revision: 1205383
- Update to version 5.2.13
- Update to mpdm-2.1.7
- Remove ANSI colors patch
* Sat Feb 17 2018 kekepower <kekepower> 5.2.12-1.mga7
+ Revision: 1202381
- Have to define the upstream_name since the rename of the project
- Complete the renaming to mp
- Provides mp-5
- Rename spec file from mp-5.spec to mp.spec
- Rename project from mp-5 to mp
- Renamed patch
- Update to 5.2.12 final
- Fixed a version naming error
- Fixed %%setup_compile_flags
- Added %%docs
- Added %%find_lang
* Fri Feb 16 2018 kekepower <kekepower> 5.2.12dev-0.20180212_gitce894e5.1.mga7
+ Revision: 1201702
- Update to version 5.2.12dev-0.20180212_gitce894e5
- Add patch to enable ANSI colors
* Fri Feb 16 2018 kekepower <kekepower> 5.2.11-3.mga7
+ Revision: 1201693
- Added BR for grutatxt, which in turn builds the man page
* Thu Feb 15 2018 kekepower <kekepower> 5.2.11-2.mga7
+ Revision: 1201595
- Added BR for pcre-devel
- Added a few more configure options
- Fixed the %%files section a little
* Thu Feb 01 2018 kekepower <kekepower> 5.2.11-1.mga7
+ Revision: 1198468
- Add bison BR
- Add flex BR
- imported package mp-5
