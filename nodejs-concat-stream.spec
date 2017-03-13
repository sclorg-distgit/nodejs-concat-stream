%{?scl:%scl_package nodejs-concat-stream}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       %{?scl_prefix}nodejs-concat-stream
Version:    1.5.2
Release:    1%{?dist}
Summary:    Writable stream that concatenates data and calls a callback with the result
License:    MIT
URL:        https://github.com/maxogden/node-concat-stream
Source0:    http://registry.npmjs.org/concat-stream/-/concat-stream-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}runtime
BuildRequires:  %{?scl_prefix}nodejs-devel

%description
%{summary}.

%prep
%setup -q -n package
%nodejs_fixdep inherits
%nodejs_fixdep readable-stream

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/concat-stream
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/concat-stream

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/tape test/*.js test/server/*.js
%endif

%files
%doc LICENSE readme.md
%{nodejs_sitelib}/concat-stream

%changelog
* Thu Sep 22 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.5.2-1
- Updated with script
- remove patches

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.4.4-7
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.4.4-6
- Rebuilt with updated metapackage

* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 1.4.4-5
- Enable SCL macros

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.4.4-2
- add missing BR: npm(inherits)

* Thu Mar 13 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.4.4-1
- initial package
