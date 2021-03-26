Name:           nem-nem
Version:        2011.05.1
Summary:        A dice game like Yam's or Yahtzee
Release:        5.4
License:        GPLv3
Group:          Games/Boards
URL:            http://code.google.com/p/nem-nem/
Source0:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/nem-nem/%{name}-%{version}.tar.gz
BuildRequires:  qt4-devel
BuildRequires:  sox
Requires:	sox

%description
Nem-Nem is a graphical dice game with sounds, animations and a lot of
customizing options.

%files
%_datadir/nem-nem
%_bindir/nem-nem
%_datadir/applications/nem-nem.desktop
%_datadir/pixmaps/nem-nem.png

%prep
%setup -q

%build
%qmake_qt4 nem-nem.pro
make

%install
rm -rf %buildroot
%__mkdir -p  %buildroot%_datadir/nem-nem
%__cp nem-nem %buildroot%_datadir/nem-nem/
%__cp *.qm  %buildroot%_datadir/nem-nem/
%__mkdir -p %buildroot%_datadir/nem-nem/images
%__cp images/* %buildroot%_datadir/nem-nem/images
%__mkdir -p %buildroot%_bindir
ln -s %_gamesdatadir/nem-nem/nem-nem %buildroot%_bindir
%__mkdir -p %buildroot%_datadir/applications
%__cp desktop/nem-nem.desktop %buildroot%_datadir/applications/nem-nem.desktop
%__mkdir -p %buildroot%_datadir/pixmaps
%__cp desktop/nem-nem.png %buildroot%_datadir/pixmaps/nem-nem.png

%clean
rm -rf %{buildroot}

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2011.05.1
- Rebuild for Fedora
* Thu May 26 2011 Gilles Pascual <gpascual@mandriva.org> 2011.05.1-1mdv2010.2
- Bug fix in sources when running Nem-Nem under OS2
- Bug fix in save format
* Wed May 25 2011 Gilles Pascual <gpascual@mandriva.org> 2011.05.1b-1mdv2010.2
- New human readable save format
* Sun Mar 27 2011 Gilles Pascual <gpascual@mandriva.org> 2011.03.4-1mdv2010.1
- SPEC update
* Mon Mar 21 2011 Gilles Pascual <gpascual@mandriva.org> 2011.03.2-1mdv2010.1
- SPEC update
* Sat Jul 03 2010 Gilles Pascual <gpascual@mandriva.org> 2010.07.1-1mdv2010.1
- Bug fix on undo management
- Improve Robot play
* Sat Jun 05 2010 Gilles Pascual <gpascual@mandriva.org> 2010.06.1-1mdv2010.1
- No more row CHANCE, replace by 2 new rows. 1 new column, demo mode.
* Wed Mar 24 2010 Gilles Pascual <gpascual@mandriva.org> 2010.03-1mdv2010.1
- Sounds in Nem-Nem
* Sun Feb 07 2010 Gilles Pascual <gpascual@mandriva.org> 2010.01.4-1mdv2010.1
- Some display optimizations
* Thu Jan 28 2010 Gilles Pascual <papajaac@gmail.com> 2010.01.3-1mdv2010.1
- New menu action + ESC key to return from help page, preferences... to main page
* Thu Jan 28 2010 Stephane Téletchéa <steletch@mandriva.org> 2010.01.1-2mdv2010.1
- Spec corrections and updates
* Wed Jan 27 2010 Gilles Pascual <gpascual@laposte.net> 2010.01.1-1mdv2010.1
- Initial Mandriva package
