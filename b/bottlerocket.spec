%undefine _debugsource_packages

Name:          bottlerocket
Version:       0.04c
Release:       6.1
Summary:       A commandline interface to the X-10 Firecracker device
License:       GPL
Group:         Hardware/Other
URL:           https://www.linuxha.com/bottlerocket/
Source:        %{name}-current.tar.bz2
Source1:       README.SUSE-%name
Patch0:         %{name}-destdir.patch

%description
BottleRocket is a command-line interface for Unix systems to use the X-10
FireCracker kit. It is easy to use, has all of the major (non-gui)
functionality of the Windows interface, is easy to call from scripts and the
backend code is made to be easily linked into other programs.

Authors:
-------
    Neil Cherry <ncherry@linuxha.com>
    Ashley Clark <aclark@ghoti.org>
    Tymm Twillman <tymm@acm.org>

%prep
%setup -q
%patch 0 -p1

%build
cp %{SOURCE1} README.SUSE
export CFLAGS="$RPM_OPT_FLAGS"
./configure \
        --prefix=/usr \
        --with-x10port=/dev/firecracker

CFLAGS=$RPM_OPT_FLAGS make

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/dev
cd $RPM_BUILD_ROOT/dev
ln -sf ttyS0 firecracker

%files
%doc README INSTALL README.SUSE
%{_bindir}/br
%config(noreplace) /dev/firecracker

%changelog
* Sun Jan 20 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.04c
- Rebuilt for Fedora
* Wed Aug 16 2006 - James Oakley <jfunk@funktronics.ca> - 0.04c-1
- Build under buildservice
* Thu May 12 2005 - James Oakley <jfunk@funktronics.ca> - 0.04c-ft.2
- Build for SL93
* Fri Nov 19 2004 - James Oakley <jfunk@funktronics.ca> - 0.04c-ft.1
- Build for SL92
* Wed May 12 2004 - James Oakley <jfunk@funktronics.ca> - 0.04c-4
- Build for SL9
* Thu Oct 30 2003 - James Oakley <jfunk@funktronics.ca> - 0.04c-3
- Build for SUSE 9.0
* Mon May 26 2003 - James Oakley <jfunk@funktronics.ca> - 0.04c-2
- Build for SuSE 8.2
* Tue Dec 31 2002 - James Oakley <jfunk@funktronics.ca> - 0.04c-1
- Initial Package
