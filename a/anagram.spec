Name:                   anagram
Version:                1.16
Summary:                Anagram finder
License:                Public Domain
URL:                    https://sourceforge.net/projects/anagram/
Source:                 anagram-1.16.tar.gz
Group:                  Productivity/Text/Utilities
Release:                3.1
Patch0:                 anagram-1.16-headers_fix.diff

%description
anagram is a fast command-line C program to find all possible anagrams of a
word or phrase that can be made from the words on the system or a user-supplied
wordlist.It was developed on Unix in 1985 and should compile and run on almost
anything.

%prep
%setup -q
%patch 0 -p1

%build
gcc %{optflags} -o anagram anagram.c

%install
%{__rm} -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{name} $RPM_BUILD_ROOT/%{_bindir}

%files
%{_bindir}/%{name}

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.16
- Rebuilt for Fedora
* Mon Jun 28 2010 David Bolt <davjam@davjam.org> 1.16
- First packaged for openSUSE
