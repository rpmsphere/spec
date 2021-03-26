Name:		gtkperf
Summary:	GTK+ performance tester
Summary(ru_RU.UTF-8): Утилита для тестирования производительности модулей прорисовки GTK+
Version:	0.40
Release:	4.1
License:	GPLv2
Group:		System/X11
Source0:	%{name}-%{version}.tar.gz
Source1:        gtkperf.desktop
URL:		http://gtkperf.sourceforge.net/
BuildRequires:  gcc-c++ desktop-file-utils gtk2-devel

%description
GtkPerf is an application designed to test GTK+ performance. The point
is to create common testing platform to run predefined GTK+ widgets
and this way define the speed of device/platform.

%description -l ru_RU.UTF-8
Данный пакет содержит в себе утилиту GtkPerf предназначенную для тестирования 
производительности модулей прорисовки GTK+. 

%prep
%setup -q
sed -i 's|g_printf (timestring);|g_printf ("%s", timestring);|' src/timing.c

%build
%configure
# Do not run autoheader
touch ./stamp-h*

# A bug in configure.in makes CFLAGS to be overwritten with an empty string
# so set CFLAGS in make
make CFLAGS="%{optflags}"

# Changelog must be converted to utf8
rm -f ./ChangeLog.utf8
iconv -f ISO-8859-1 -t utf8 ./ChangeLog -o ChangeLog.utf8
mv -f ChangeLog.utf8 ./ChangeLog

%install
%make_install
mv %{buildroot}/usr/doc %{buildroot}%{_datadir}/doc
desktop-file-install --vendor=""	\
	--dir=%{buildroot}%{_datadir}/applications\
        --remove-category=System \
        --add-category=Development \
        --add-category=Profiling \
	%{SOURCE1}

%files
%{_docdir}/%{name}
%{_bindir}/*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*

%changelog
* Thu Jan 12 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.40
- Rebuild for Fedora
* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.40-alt1.qa3
- NMU: rebuilt for updated dependencies.
* Sat May 21 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.40-alt1.qa2
- NMU: fix desktop permissions
* Wed May 18 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.40-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gtkperf
  * postclean-03-private-rpm-macros for ([not specified])
  * postclean-05-filetriggers for ([not specified])
* Wed Jul 01 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.40-alt1
- First build for Sisyphus
