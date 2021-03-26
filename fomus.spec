Summary: Music notation software package
Name: fomus
Version: 0.1.18
Release: 0.alpha
License: GPL
Group: Applications/Multimedia
URL: http://fomus.sourceforge.net/
Source0: fomus-%{version}-alpha.tar.gz
Patch0: fomus-0.1.18-gcc4.7.patch
BuildRequires: boost-devel boost-filesystem lilypond ncurses-devel libtool-ltdl-devel swig

%description
FOMUS is a notation software package that automates many musical
notation tasks. It is designed to facilitate the process of creating a
professionally notated score from computer music software
languages/environments such as CM/Grace, Pd, Lisp, etc.. It can also
be used for other tasks such as creating scores from MIDI files or
from scratch.

%prep
%setup -q -n fomus-%{version}-alpha
%patch0 -p1
%ifarch x86_64 aarch64
sed -i -e 's|/lib |/lib64 |g' -e 's|/lib"|/lib64"|' configure
%endif

%build
%configure
make CXXFLAGS+=-std=gnu++98

%install
rm -rf $RPM_BUILD_ROOT
make %{?_smp_mflags} DESTDIR=$RPM_BUILD_ROOT install
mv $RPM_BUILD_ROOT%{_datadir}/doc/fomus $RPM_BUILD_ROOT%{_datadir}/doc/fomus-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/fomus
%{_includedir}/fomus.h
%{_includedir}/fomus
%{_libdir}/fomus
%{_libdir}/libfomus.*
%{_datadir}/fomus
%{_datadir}/emacs/site-lisp/fomus.el
%{_datadir}/doc/fomus-%{version}

%changelog
* Mon Mar 30 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.18-alpha
- Rebuild for Fedora
* Wed Jun 27 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.18-1.alpha
- update to 0.1.18, add patch to build with gcc 4.7
* Tue May 31 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.17-1.alpha
- update to 0.1.17
* Sun Mar 20 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.16-1.alpha
- update to 0.1.16 to fix boost problems in fc14
* Fri Mar 18 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.15-1.alpha
- update to 0.1.15 alpha.
* Tue Mar 15 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.14-1.alpha
- update to 0.1.14 alpha.
* Thu Dec  9 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.13-1.alpha
- new version includes proper fix for fc14
* Wed Dec  8 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.12-1.alpha
- updated to 0.1.12-alpha
- added boost patch to fix building on fc14
* Thu Dec  2 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.12-1.alpha.rc6
- updated to 0.1.12-alpha-rc6
* Tue Oct 27 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.9-1.alpha
- updated to 0.1.9-alpha
* Thu Oct 22 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.8-1.alpha
- initial build.
