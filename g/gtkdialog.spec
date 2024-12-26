Name:           gtkdialog
Version:        0.8.5e
Release:        1
License:        GPL
Group:          Development/Tools
Source0:       %{name}-%{version}.tar.gz
Patch0:         vte_config.patch
URL:            https://github.com/puppylinux-woof-CE/gtkdialog
Summary:        GUI creation tool for shells and arbitrary interpreters. 
Summary(de):    GUI-Tool zur Erstellung von Shells als willkürliche Dolmetscher 
BuildRequires:  vte291-devel
BuildRequires:  help2man
BuildRequires:  texinfo

%description
The gtkdialog is uses an XML like simple language as a GUI description
language to produce dialog boxes. The program can be used with shells
and arbitrary interpreters. Example programs included for BASH and AWK.

%description -l de
Die GtkDialog ist ein XML-Anwendungen als einfache Sprache zum produzieren 
von Dialogfelder als GUI. Das Programm kann verwendet werden um komplizierte 
Konsolen Befehle zu vereinfachen. Beispiel enthaltenen Programme für bash 
und awk. 

%prep
%setup -q
#patch 0 -p1

%build
export LDFLAGS=-Wl,--allow-multiple-definition
./autogen.sh --prefix=/usr --enable-gtk3
%make_build

%install
%make_install

%files
%doc README TODO examples
%_bindir/*
%_datadir/icons/*
%_infodir/*

%changelog
* Sun Nov 17 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.5e
- Rebuilt for Fedora
* Sun Mar 08 2020 daniel <meisssw01 at gmail.com> 0.8.4-1pclos2020
- update to gtk3
- add missing BuildRequires
- add patch to get VTE support
- widget_combobox_create(): The combobox (GtkCombo) widget has been removed from GTK+ 3 and comboboxtext or comboboxentry are recommended as replacements.
* Thu Jan 24 2013 daniel <meisssw01 at gmail.com> 0.8.3-1leiche2013
- upstream tarball
* Sun Oct 21 2012 daniel <meisssw01 at gmail.com> 0.8.2-2leiche2012
- compiled with vte support
* Sun Sep 30 2012 daniel <meisssw01 at gmail.com> 0.8.2-1leiche2012
- upstream tarball
* Thu Dec 09 2010 leiche <meisssw01 at aol.com> 0.7.20-8leiche2010
- add german language description
- convert archive as tar.xz
* Sun Oct 04 2009 Texstar <texstar at gmail.com> 0.7.20-7pclos2010
- rebuild
* Wed May 20 2009 Texstar <texstar at gmail.com> 0.7.20-6pclos2009
- recreate missing package
* Fri Feb 22 2008 Nico Reuter <nico at sam-linux.org> 0.7.20-5pclos2007
- removed "provides: gtkdialog"
 