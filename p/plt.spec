Summary: A command-line utility for creating X11 and PostScript plots of data
Name: plt
Version: 2.5a
Release: 11.1
Source0: http://www.physionet.org/physiotools/plt/%{name}-%{version}.tar.gz
License: GPL
URL: http://www.physionet.org/physiotools/plt/
Group: Applications/Engineering
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: xorg-x11-proto-devel
BuildRequires: libX11-devel

%description
`plt' is a command-line, scriptable plotting utility originally written for
Unix by Paul Albrecht.  `plt' can produce publication-quality 2D plots in an X
window or in PostScript from easily-produced text or binary data files.  The
package includes `pltf', which can generate function plots using `bc' and
`plt', `imageplt', which can generate plots of grey-scale images, and `lwcat',
which can generate PDF and PNG plots using `plt' or `pltf' and ImageMagick
converters.

%prep
%setup -q

%build
%ifarch x86_64
make XINCDIR=/usr/include XLIBDIR=/usr/lib64
%else
make XINCDIR=/usr/include XLIBDIR=/usr/lib
%endif

%install
rm -rf %{buildroot}
make INSTALL_PREFIX=%{buildroot}%{_prefix} PREFIX=%{_prefix} MAN1DIR=%{buildroot}%{_mandir}/manl PSPDIR=%{buildroot}/usr/lib/ps install
sed -i 's|%{buildroot}||g' %{buildroot}%{_bindir}/lwcat %{buildroot}%{_bindir}/plt

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
/usr/lib/ps/*
%{_mandir}/manl/*.1.*

%changelog
* Sun Mar 31 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5a
- Rebuilt for Fedora
* Wed Apr 27 2005 George B Moody <george@mit.edu>
- updated spec to work with updated Makefiles
* Thu May 01 2003 George B Moody <george@mit.edu>
- added lwcat man page, updated doc/book.tex
* Wed Feb 26 2003 George B Moody <george@mit.edu>
- added imageplt source, example, and man page
- avoid installing man pages in mandir to avoid conflict with wfdb-doc
* Thu Oct 17 2002 George B Moody <george@mit.edu>
- Updated summary and package description, added missing files
* Thu Oct 17 2002 Isaac C Henry <ihenry@physionet.org>
- fixed install command to use temporary rpm build root
- changed '%files' listings to use rpm's path variables
* Fri Oct 1 2002 George B Moody <george@mit.edu>
- 'make rpms' now works
* Mon Apr 1 2002 Isaac C Henry <ihenry@physionet.org>
- Initial rpm build
