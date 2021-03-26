%global debug_package %{nil}

Summary: Yet another Motif file manager
Name: xplore
Version: 1.2a
Release: 11.1
License: GPL
Group: Applications/File
Source: http://www.musikwissenschaft.uni-mainz.de/~ag/xplore/xplore-%{version}.tar.gz
URL: http://www.musikwissenschaft.uni-mainz.de/~ag/xplore/
BuildRequires: imake
BuildRequires: libXpm-devel
BuildRequires: libXmu-devel
BuildRequires: motif-devel

%description
Xplore file manager, linked dynamically with OpenMotif 2.2.

Xplore is a powerful and highly configurable Motif file manager with
an Explorer-like user interface. The package includes configuration
files, a man page and many icons. Author: Albert Graef
<ag@muwiinfa.geschichte.uni-mainz.de>.

%prep
%setup -q
sed -i '198d' regexp/regexp.c
sed -i '20i #ifndef XmS_MOTIF_EXPORT_TARGETS\n#define XmS_MOTIF_EXPORT_TARGETS ((char *)&_XmStrings[17220])\n#endif' callbacks.c
sed -i '303i return NONE;' ftype.c

%build
xmkmf -a
make

%install
make DESTDIR=$RPM_BUILD_ROOT install install.man

%clean 
rm -rf $RPM_BUILD_ROOT 

%files
%doc ChangeLog COPYING INSTALL README TODO
%{_bindir}/xplore
%{_bindir}/xploretype
%{_mandir}/man1/xplore.1*
%{_mandir}/man1/xploretype.1*
%exclude /usr/lib/X11/app-defaults
%{_datadir}/X11/app-defaults/Xplore
/usr/lib/X11/xplore

%changelog
* Fri Jun 05 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2a
- Rebuild for Fedora
* Thu Aug 14 2003 Albert Graef <ag@muwiinfa.geschichte.uni-mainz.de>
- Initial package
