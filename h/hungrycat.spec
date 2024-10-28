Name:           hungrycat
Version:        0.4.1
Release:        3.1
Summary:        Cat and rm in a single Tool
Source:         https://jwilk.net/pool/hungrycat-%{version}.tar.gz
URL:            https://jwilk.net/software/hungrycat.html
Group:          System/Base
License:        GNU General Public License version 2 (GPL v2)
BuildRequires:  gcc make glibc-devel

%description
hungrycat is a tool that prints the contents of a file on the standard output
while simultaneously freeing disk space occupied by the file. It can be useful
if you need to process a large file, but you don't have enough space to store
the output file, and you won't need the input file afterward.

Authors:
--------
    Jakub Wilk <ubanus@users.sf.net>

%prep
%setup -q

%build
%configure
make %{?jobs:-j%{jobs}} \
     CC="%__cc" \
     OPTFLAGS="%{optflags}"

%install
rm -rf "$RPM_BUILD_ROOT"
install -D -m0755 hungrycat "$RPM_BUILD_ROOT%{_bindir}/hungrycat"

%files
%doc doc/README doc/changelog
%{_bindir}/hungrycat

%changelog
* Wed Apr 11 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.1
- Rebuilt for Fedora
* Sat Nov 13 2010 pascal.bleser@opensuse.org
- update to 0.2:
  * error handling was improved
* Fri Dec  4 2009 pascal.bleser@opensuse.org
- initial version
