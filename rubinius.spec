Name: rubinius
Version: 3.14
Release: 1
License: BSD
Group: Development/Languages/Ruby
URL: http://rubini.us
BuildRequires: llvm34-static
BuildRequires: llvm34-devel
BuildRequires: rubygems rubygem-rake rubygem-bundler rubygem-psych
BuildRequires: gcc-c++ zlib-devel openssl-devel readline-devel
BuildRequires: ruby-devel
BuildRequires: rubypick
BuildRequires: libyaml-devel
Source0: http://releases.rubini.us/%{name}-%{version}.tar.bz2 
Summary: A virtual machine for running Ruby programs and a Ruby core library

%description
Rubinius is a virtual machine and compiler for Ruby created by Evan Phoenix.
Based loosely on the Smalltalk-80 Blue Book design, Rubinius seeks to provide
a rich, high-performance environment for running Ruby code.

%prep
%setup -q
sed -i 's|-Werror|-Wno-error|' rakelib/blueprint.rb

%build
bundle install --local
./configure --prefix=%{_libdir} --bindir=%{_bindir} --mandir=%{_mandir} --includedir=%{_includedir}/rubinius --disable-llvm CFLAGS=-Wno-error CXXFLAGS=-Wno-error \
%ifarch x86_64
--llvm-config=/usr/bin/llvm-config-64-3.4 --with-include-dir=/usr/include/llvm34
%else
--llvm-config=/usr/bin/llvm-config-32-3.4 --with-include-dir=/usr/include/llvm34
%endif
bundle exec rake build

%install
rake install DESTDIR=%{buildroot}

%clean
%{__rm} -fr %{buildroot}

%files
%doc README LICENSE AUTHORS THANKS
%{_libdir}/rubinius

%changelog
* Wed Feb 03 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 3.14
- Rebuild for Fedora
* Mon Jul 25 2011 Duncan Mac-Vicar <dmacvicar@suse.de>
- update to 1.2.4
- see http://rubini.us/releases/1.2.4 
* Thu Jun 16 2011 Duncan Mac-Vicar <dmacvicar@suse.de>
- update to 1.2.3
* Wed Dec 22 2010 Duncan Mac-Vicar <dmacvicar@suse.de>
- update to 1.2.0
- see http://rubini.us/releases/1.2.0
