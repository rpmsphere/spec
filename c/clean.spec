%undefine _debugsource_packages

Name: clean
Version: 3.1
Release: 1
Summary: The Clean programming language compiler and environment
Summary(ru_RU.UTF-8): Компилятор и системная библиотека для языка Clean
License: BSD license
Group: Development/Functional
URL: https://clean.cs.ru.nl/
#BuildRequires: prelink-tools
BuildRequires: execstack
Source: clean-%version.tar
Patch0: %name-3.0-alt-remove-doc-build.patch

%description
This package contains a Clean language compiler and standard
library. This is a bootstrap package for 64-bit intel architecture.

%prep
%setup -q
%patch 0 -p2

%build
./clean-base/linux-x64/build.sh clean-base linux x64
cd target/clean-base/lib/StdEnv/
for f in `ls *.icl`; do
  PATH=$PATH:../../bin/ CLEANLIB=../exe clm -dynamics -I . -PO `echo $f | sed s/.icl//`
done
PATH=$PATH:../../bin/ CLEANLIB=../exe clm -dynamics -I . -PO StdEnv
cd ../../../../
execstack -c target/clean-base/lib/exe/cg
execstack -c target/clean-base/lib/exe/cocl
cd src/clm-master
make -fMakefile.linux64 CLEANLIB=%_libdir/%name/exe/ CLEANPATH=.:%_libdir/%name/StdEnv/ clms
cp clms ../../target/clean-base/bin/clm

%install
%define docdir %_docdir/%name-%version
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_libdir/%name
mkdir -p %buildroot%docdir
mkdir -p %buildroot%_mandir
%define target target/clean-base/
install -pm755 %target/bin/* %buildroot/%_bindir/
cp -R %target/lib/* %buildroot%_libdir/%name
cp src/language-report-master/CleanRep.3.0.doc %buildroot%docdir
cp src/language-report-master/todo.txt %buildroot%docdir
cp src/clean-ide-master/CleanLicenseConditions.txt %buildroot%docdir
cp clean-base/linux-x64/txt/README %buildroot%docdir/README.md
install -pm644 src/clm-master/clm.1 %buildroot%_mandir

%post
# Touching compiled files to prevent autogeneration
touch "/usr/lib64/clean/StdEnv/Clean System Files"/*.abc
sleep 1
touch "/usr/lib64/clean/StdEnv/Clean System Files"/*.o

%files
%_bindir/*
%_libdir/*
%_mandir/*
%docdir

%changelog
* Sun Oct 02 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 3.1
- Rebuilt for Fedora
* Sun Oct 02 2022 Andrey Bergman <vkni@altlinux.org> 3.1-alt3
- Update to intermediate release.
* Tue Jul 05 2022 Andrey Bergman <vkni@altlinux.org> 3.1-alt2
- Update to intermediate release.
* Sun Feb 06 2022 Andrey Bergman <vkni@altlinux.org> 3.1-alt1
- Update to 3.1 version. Enabled dynamics.
* Thu Jan 28 2021 Andrey Bergman <vkni@altlinux.org> 3.0-alt1.7
- Update to recent unstable version.
* Wed Oct 28 2020 Andrey Bergman <vkni@altlinux.org> 3.0-alt1.6
- Update to recent unstable version.
* Wed Sep 30 2020 Andrey Bergman <vkni@altlinux.org> 3.0-alt1.5
- Update to recent unstable version.
* Sun Jan 26 2020 Andrey Bergman <vkni@altlinux.org> 3.0-alt1.4
- Update to recent unstable version.
* Thu Dec 05 2019 Andrey Bergman <vkni@altlinux.org> 3.0-alt1.3
- Update to recent unstable version. Remove linker in favor of ld.
* Sat May 11 2019 Andrey Bergman <vkni@altlinux.org> 3.0-alt1.2
- Bake in paths into clm, update compiler.
* Fri May 03 2019 Andrey Bergman <vkni@altlinux.org> 3.0-alt1.1
- Add exclusive arch
* Thu May 02 2019 Andrey Bergman <vkni@altlinux.org> 3.0-alt1
- Initial release for Sisyphus.
