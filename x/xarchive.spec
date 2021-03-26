Name: xarchive
Version: 0.2.8
Summary: XArchive Manager
Group: File tools
License: BSD
URL: http://xarchive.sourceforge.net/
Release: 13.1
Source0: http://prdownloads.sourceforge.net/xarchive/%{name}-%{version}-6.tar.gz
BuildRequires: freetype-devel gtk2-devel pango-devel

%description
XArchive is a little different from your average bear.
You see, it's not designed for any specific set of command line archiving tools.
Instead XArchive uses external wrappers to talk to the command line tools.
When XArchive starts up it checks it's wrapper directory, consulting each wrapper
found to see if the appropriate command line tools are installed and, if so, what
file types are supported. This means that a new archive format can easily be
supported by just writing a wrapper for it's command line tool and dropping it in
the wrappers directory.

Currently there are bash shell wrappers for: rar, tar, zip, and ace(ace supported
using unace, so only reading and extracting available). Having these wrappers as
fairly simple bash shell scripts means they are quite easily copied and modified
to add support for different tools. In fact, once I had the tar-wrap.sh written
and fully functional, making the zip-wrap.sh, rar-wrap.sh, and ace-wrap.sh from
it took less than an hour.

%prep
%setup -q -n %{name}-%{version}-6
sed -i '559s|text|"%%s", text|' src/widgets_gtk.c
sed -i '1889s|msg|"%%s", msg|' src/widgets_gtk.c

%build
%configure
%__make %{?_smp_mflags}

%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT
sed -i 's|multipart/x-zip;||' $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
sed -i 's|/usr/share/pixmaps/%{name}.xpm|%{name}|' $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/doc/%{name}
%{_datadir}/man/man1/%{name}.1.gz
%{_datadir}/pixmaps/%{name}.xpm

%clean
%__rm -rf $RPM_BUILD_ROOT

%Changelog
* Wed Aug 15 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.8
- Rebuild for Fedora
* Fri Dec 02 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.2.8-alt1
- 0.2.8
* Tue Nov 15 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.2.6-alt1
- 0.2.6
- remove generation .menu files from .desktop
* Tue Jul 05 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.1.8-alt1
- build for ALT Linux
