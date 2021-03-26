%define oname	FileRunner
%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}
# We ship with inotify binaries for x86 and x86_64 however the code
# detects which, if either, is useful and uses that one or none.
# We also ship, in the package, the means to build the inotify binary
# after the package is installed.
Autoreq: 0
%define _binaries_in_noarch_packages_terminate_build   0

Summary:	A simple file manager with built-in FTP, SFTP and adb support
Name:		filerunner
Version:        20.05.02.17
Release:	1
License:	GPLv2+
URL:		http://sourceforge.net/projects/%{name}/
Source0:	http://downloads.sourceforge.net/project/%{name}/fr-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	tcl
Requires:	tcl
Requires:       tcllib
Requires:	tk
Requires:       tklib
Provides:	%{oname} = %{version}-%{release}
Obsoletes:	%{oname} <= 2.5.1

%postun
if [ -e %{_datadir}/doc/${name}} ] ; then
    rmdir --ignore-fail-on-non-empty %{_datadir}/doc}
fi

%post
for file in  %{_datadir}/doc/%{name}/*.gz ; do  gunzip -f $file ; done
if [ ! -e %{_datadir}/config/filerunnerrc ] ; then 
mkdir -p  %{_datadir}/config
cat > %{_datadir}/config/filerunnerrc <<EOF
# Put global filerunner configure stuff here
EOF
fi
arch=`arch`
if [ -e %{_datadir}/filerunner/packages/inotify/$arch ] ; then
mv %{_datadir}/filerunner/packages/inotify/$arch/* %{_datadir}/filerunner/packages/inotify/
rm -rf %{_datadir}/filerunner/packages/inotify/*/
rm -f %{_datadir}/filerunner/Makefiles/tcl-inotify-*
rm -f %{_datadir}/filerunner/Makefiles/build_inotify
if [ -d %{_datadir}/filerunner/Makefiles] ] ; then rmdir --ignore-fail-on-non-empty %{_datadir}/filerunner/Makefiles; fi
else
rm -rf %{_datadir}/filerunner/packages/inotify
fi

%description
FileRunner is a very configurable file manager for Unix. It is simple and
efficient and has a built-in FTP, SFTP and adb clients. New and improved 
from a FileRunner of long ago.

%prep
%setup -q -c

%build

%install
export DONT_STRIP=1
cd %{name}/Makefiles
./INSTALL DESTDIR=%{buildroot} -nogui %{?_verb}

%clean
rm -rf %{buildroot}

%files
%{_datadir}/doc/%{name}
%{_bindir}/fr
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}


%changelog
* Tue May 05 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 20.05.02.17
- Rebuild for Fedora
