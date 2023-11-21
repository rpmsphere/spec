Name:         gnuit
Summary:      GNU Interactive Tools
URL:          https://www.gnu.org/software/gnuit/
Group:        Terminal
License:      GPL
Version:      4.9.5
Release:      9.1
Source0:      ftp://ftp.gnu.org/gnu/gnuit/gnuit-%{version}.tar.gz

%description
GNU Interactive Tools (GnuIT) is a set of interactive text-mode
tools, closely integrated with the shell. It contains an extensible
file system browser, an ASCII/Hex file viewer, a process
viewer/killer and some other related utilities and shell scripts.

%prep
%setup -q
sed -i 's|printf(copyright);|printf("%s", copyright);|' src/git.c

%build
autoreconf -ifv

./configure \
    --prefix=%{_prefix} \
    --mandir=%{_mandir} \
    --infodir=%{_infodir}
%{__make} %{_smp_mflags -O}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"
mv  $RPM_BUILD_ROOT%{_bindir}/git \
    $RPM_BUILD_ROOT%{_bindir}/gnuit
mv  $RPM_BUILD_ROOT%{_mandir}/man1/git.1 \
    $RPM_BUILD_ROOT%{_mandir}/man1/gnuit.1
#rm -rf $RPM_BUILD_ROOT%{_prefix}/share/doc
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
#rm -f $RPM_BUILD_ROOT%{_prefix}/lib/charset.alias
rm -f $RPM_BUILD_ROOT%{_bindir}/.gitaction

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/doc/%{name}
%{_infodir}/*
%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 4.9.5
- Rebuilt for Fedora
