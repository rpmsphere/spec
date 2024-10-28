Name:               dehtml
Version:            1.8
Release:            3.1
Summary:            Removes HTML Contructs from Documents
Source:             https://www.moria.de/~michael/dehtml/dehtml-%{version}.tar.gz
Patch1:             dehtml-add_destdir_and_remove_strip.patch
Patch2:             dehtml-fix_missing_return_in_nonvoid_function.patch
URL:                https://www.moria.de/~michael/dehtml/
Group:              Productivity/Text/Convertors
License:            GNU General Public License version 2 or later (GPL v2 or later)
BuildRequires:      gcc make glibc-devel pkgconfig
BuildRequires:      autoconf automake libtool

%description
Dehtml removes HTML constructs from documents for indexing, spell checking and
so on. My own implementation is a little smarter than the other implementations
I have seen, because it knows about certain tags and expands entities to Latin
1 characters. It is able to generate a word list for spell checking tools and
to omit headers for sentence analysis tools. 

%prep
%setup -q
%patch 1
%patch 2

%build
%configure
# -j breaks the build
%__make

%install
%__rm -rf "$RPM_BUILD_ROOT"
make DESTDIR=$RPM_BUILD_ROOT install
%find_lang "%{name}"

%files -f "%{name}.lang"
%doc COPYING NEWS README
%{_bindir}/dehtml
%doc %{_mandir}/man1/dehtml.1.*
%lang(de) %doc %{_mandir}/de/man1/dehtml.1.*

%changelog
* Fri May 11 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8
- Rebuilt for Fedora
* Tue Oct 12 2010 pascal.bleser@opensuse.org
- initial package (1.7)
