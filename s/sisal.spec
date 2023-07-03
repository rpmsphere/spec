Summary: Sisal Parallel Programming
Name: sisal
Version: 14.1.0
Release: 1
License: LLNL Notice, non-commercial
Group: Development/Language
URL: https://sisal.sourceforge.net/
Source0: https://sourceforge.net/projects/sisal/files/sisal-unix/sisal-%{version}/%{name}-%{version}.tgz
#https://pascal.eng.uci.edu/projects/sisal/sisaltutorial/
Source1: sisal-tutorial.zip

%description
Sisal is a unique parallel language that supports a clean, fully implicit
parallelization model. The optimizing sisal compiler (sisalc) works on top
of pthreads to give high performance on commodity SMP architectures.

%prep
%setup -q
sed -i -e 's|  if (!NoFibreOutput|//&|' -e 's|    fputc|//&|' Runtime/Sharedlib/srt0.c

%build
%configure
%make_build

%install
%make_install
install LICENSE.LLNL COPYRIGHT.1993 NEWS %{buildroot}%{_docdir}/%{name}
cp -a Tests %{buildroot}%{_docdir}/%{name}
unzip -q %{SOURCE1} -d %{buildroot}%{_docdir}/%{name}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%{_docdir}/%{name}
%{_bindir}/*
%{_includedir}/%{name}
%{_libdir}/%{name}
%{_libexecdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man?/*

%changelog
* Sun Sep 26 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 14.1.0
- Rebuilt for Fedora
