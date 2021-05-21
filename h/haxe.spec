Name: haxe
#Version: 3.1.3
Version: 3.0.0
Release: 6.1
Summary: An open source programming language
License: GPLv2
Group: Development/Other
URL: http://haxe.org
# https://github.com/HaxeFoundation/haxe.git
Source: %name-%version.tar
BuildRequires: ocaml-camlp4-devel zlib-devel
%define haxelib %_prefix/lib/%name

%description
While most other languages are bound to their own platform
(Java to the JVM, C# to .Net, ActionScript to the Flash Player),
Haxe (pronounced as hex) is a multiplatform language.

The idea behind Haxe is to let the developer choose the best platform
for a given job. In general, this is not easy to do,
because every new platform comes with its own programming language.

What Haxe provides you with is:
* a standardized language with many good features
* a standard library (including Date, Xml, Math...) that works the same on all platforms
* platform-specific libraries : the full APIs for a given platform are accessible from Haxe

%prep
%setup -q

%build
make

%install
#%make_install INSTALL_DIR=%buildroot%_prefix
install -D haxe %buildroot%_bindir/haxe
mkdir -p %buildroot/%haxelib/
cp -a std %buildroot/%haxelib/
# FIXME: haxelib dir
mkdir -p %buildroot/%haxelib/lib/
#mkdir %buildroot/%_localstatedir/haxe/
#chmod 755 $(INSTALL_DIR)/lib/haxe/lib
install -D std/tools/haxelib/haxelib.sh %buildroot%_bindir/haxelib
install -D std/tools/haxedoc/haxedoc.sh %buildroot%_bindir/haxedoc

%files
%_bindir/%name
%_bindir/haxedoc
%_bindir/haxelib
%haxelib/

%changelog
* Tue Feb 17 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.0
- Rebuilt for Fedora
* Mon Aug 05 2013 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- merge with tag v3-00, real 3.0.0 version
* Fri Mar 29 2013 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt0.1
- Initial build for ALTLinux Sisyphus
