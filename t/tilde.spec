Name:           tilde
Version:        0.4.2
Release:        1
Summary:        An intuitive text editor for the terminal
License:        GPL-3.0
Group:          Development/Libraries/C and C++
URL:            http://os.ghalkes.nl/t3/libt3widget.html
Source:         http://os.ghalkes.nl/dist/%name-%version.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  libunistring-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libt3config) >= 0.2.6
BuildRequires:  pkgconfig(libt3highlight) >= 0.4.0
BuildRequires:  pkgconfig(libt3widget) >= 0.5.0
BuildRequires:  pkgconfig(libtranscript) >= 0.2.0

%description
Tilde is a text editor for the console/terminal, which provides an
intuitive interface for people accustomed to GUI environments such as
Gnome, KDE and Windows. For example, the short-cut to copy the
current selection is Control-C, and to paste the previously copied
text the short-cut Control-V can be used. As another example, the
File menu can be accessed by pressing Meta-F.

%prep
%setup -q

%build
%configure --docdir="%_docdir/%name"
make %{?_smp_mflags}

%install
b="%buildroot"
make install DESTDIR="$b"

%files
%_bindir/tilde
%_docdir/%name/
%_datadir/%name/
%_mandir/man1/tilde.1*
%doc COPYING

%changelog
* Tue Nov 06 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.2
- Rebuilt for Fedora
* Mon Aug  7 2017 jengelh@inai.de
- Update to new upstream release 0.3.7
  * Resolve crashes that happened on program exit
  * Add a "toggle comment" functionality.
  * Several problems with syntax highlighting were fixed.
* Thu Feb 19 2015 p.drouand@gmail.com
- Update to version 0.3.4
  * Re-release of version 0.3.4 to update the configure script.
* Mon Jul 21 2014 jengelh@inai.de
- Update to new upstream release 0.3.3
  * This release correctly handle errors in conversion when loading
  files. When the converter failed in unexpected ways, Tilde would
  previously crash.
  * Added warnings about trying to overwrite a read-only file,
  improved the warnings about encoding issues when saving and fixed
  the setting of the comment-keyword style.
* Mon Jun 10 2013 jengelh@inai.de
- Initial package (version 0.3.0) for build.opensuse.org
