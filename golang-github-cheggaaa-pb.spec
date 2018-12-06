# https://github.com/cheggaaa/pb
%global goipath         github.com/cheggaaa/pb
Version:                1.0.26
%global gopkg_goipath   gopkg.in/cheggaaa/pb.v1
%global gopkg_name      %gorpmname %{gopkg_goipath}

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Console progress bar for Golang
# Detected licences
# - BSD (3 clause) at 'LICENSE'
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

%description
%{summary}


%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/mattn/go-runewidth)
BuildRequires: golang(golang.org/x/sys/unix)
BuildRequires: golang(github.com/fatih/color)
BuildRequires: golang(github.com/mattn/go-colorable)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%package -n %{gopkg_name}-devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/mattn/go-runewidth)
BuildRequires: golang(github.com/fatih/color)

%description -n %{gopkg_name}-devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{gopkg_goipath} prefix.


%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .


%install
%goinstall glide.lock glide.yaml
%goinstall -i %{gopkg_goipath} -o gopkg-devel.file-list glide.lock glide.yaml


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%files -n %{gopkg_name}-devel -f gopkg-devel.file-list
%license LICENSE
%doc README.md


%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.26-1
- Release 1.0.26

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.0.12-0.7.git.git9a180eb
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-0.6.git.git9a180eb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.12-0.5.git.git9a180eb
- Upload glide.lock and glide.yaml

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.12-0.4.20170408git9a180eb
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-0.3.git9a180eb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.0.12-0.2.git9a180eb
- Extend the import path prefixes with gopkg.in/cheggaaa/pb.v1
  resolves: #1488747

* Fri Aug 25 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.0.12-0.1.git9a180eb
- Bump to upstream 9a180eb4617eb2112e01ca3fa25c61a6303afcaf
  resolves: #1440773

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitda1f27a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitda1f27a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitda1f27a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.3.gitda1f27a
- Polish the spec file
  resolves: #1405557

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.gitda1f27a
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Mar 21 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.gitda1f27a
- First package for Fedora
  resolves: #1319714
