%global __spec_install_post %{nil}
%undefine _debugsource_packages

Name: aplus-fsf
Version: 4.22
Release: 4
License: GPL
Summary: advanced APL interpreter with s interface
URL: https://www.aplusdev.org/
Group: Development/Languages
Source: https://www.aplusdev.org/Download/%name-%version-%release.tar.gz
BuildRequires: libX11-devel
BuildRequires: libnsl2-devel

%description
A+ is a Morgan Stanley array programming environment that includes 
a rich set of functions and operators, handling of files as ordinary 
arrays, a GUI with many widgets and automatic synchronization of 
widgets and variables (using MStk in A+ Version 4), generalized 
spreadsheet-like interactions, asynchronous execution of functions 
that have been associated with variables and events, interprocess 
communication, calls to user C subroutines, and many other features. 
Execution is by a very efficient interpreter. 

%prep
%setup -q
sed -i '132,133d' src/MSIPC/MSProtocolConnection.C
sed -i 's/|| errnum > sys_nerr//' src/dap/error.c
sed -i 's|#if defined(HAVE_SVR4)|#if !defined(HAVE_SVR4)|' src/dap/sgnlcatch.c src/dap/sgnldefault.c src/dap/sgnlignore.c src/dap/sgnloriginal.c
%ifarch aarch64
cp -f /usr/lib/rpm/redhat/config.* .
%endif
sed -i '1496s|>0|!=0|' src/MSGUI/MSGraphUI.C
sed -i 's|mp>0|mp!=0|' src/MSTypes/MSBinaryMatrix.C
sed -i '11i #include <cstddef>' src/MSTypes/MSTypeData.H
sed -i 's|$(prefix)/|$(prefix)/share/aplus-fsf/|' src/{acore,autils,contrib}/Makefile*
sed -i 's|/acore|/share/aplus-fsf/acore|' src/main/aplus_main.c src/IPC/IPCInterface.C

%build
export CXXFLAGS="-O2 -fpermissive -Wno-narrowing -fPIE -fPIC -lX11" CFLAGS="-O2 -Wno-narrowing -fpermissive -fPIE -fPIC -lX11"
%ifarch aarch64
autoreconf -ifv
%endif
./configure --prefix=/usr
sed -i 's|-L | |' Makefile */Makefile */*/Makefile
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_docdir}/%{name} %{buildroot}%{_datadir}/fonts %{buildroot}%{_datadir}/X11/fonts/misc %{buildroot}%{_libdir}/%{name}
#mv %{buildroot}/usr/acore  %{buildroot}/usr/autils %{buildroot}/usr/contrib %{buildroot}/usr/lisp.* %{buildroot}%{_datadir}/%{name}
mv %{buildroot}/usr/doc %{buildroot}/usr/lisp.? %{buildroot}%{_docdir}/%{name}
mv ANNOUNCE AUTHORS ChangeLog LICENSE README %{buildroot}%{_docdir}/%{name}
mv %{buildroot}/usr/fonts/TrueType/KAPL.TTF %{buildroot}%{_datadir}/fonts
mv %{buildroot}/usr/fonts/X11/*/* %{buildroot}%{_datadir}/X11/fonts/misc
mv %{buildroot}/usr/lib/lib* %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}/etc/ld.so.conf.d
echo %{_libdir}/%{name} > %{buildroot}/etc/ld.so.conf.d/%{name}-%{arch}.conf

%files
%exclude /usr/app-defaults/XTerm
%{_docdir}/%{name}
%{_bindir}/a+
%{_datadir}/%{name}
%{_datadir}/fonts/*
%{_datadir}/X11/fonts/misc/*
%{_includedir}/a
%{_libdir}/%{name}
/etc/ld.so.conf.d/%{name}-%{arch}.conf

%changelog
* Sun Mar 12 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 4.22
- Rebuilt for Fedora
