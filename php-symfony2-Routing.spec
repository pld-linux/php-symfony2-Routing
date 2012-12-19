%define		status		stable
%define		pearname	Routing
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Symfony2 Routing Component
Name:		php-symfony2-Routing
Version:	2.1.4
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	d185e28cb56be807e2c421900faf9a5b
URL:		http://symfony.com/doc/current/components/routing/index.html
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear >= 4:1.3.10
Suggests:	php-symfony2-Config
Suggests:	php-symfony2-Yaml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Config.*) pear(Yaml.*)

%description
Symfony2 Routing Component

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

# no packaging of tests
rm -r .%{php_pear_dir}/Symfony/Component/%{pearname}/Tests
rm .%{php_pear_dir}/Symfony/Component/%{pearname}/phpunit.xml.dist

# fixups
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/CHANGELOG.md .
rm .%{php_pear_dir}/Symfony/Component/%{pearname}/.gitattributes
rm .%{php_pear_dir}/Symfony/Component/%{pearname}/.gitignore
mv docs/%{pearname}/Symfony/Component/%{pearname}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/Symfony/Component/Routing
%{php_pear_dir}/Symfony/Component/Routing/*.php
%{php_pear_dir}/Symfony/Component/Routing/Annotation
%{php_pear_dir}/Symfony/Component/Routing/Exception
%{php_pear_dir}/Symfony/Component/Routing/Generator
%{php_pear_dir}/Symfony/Component/Routing/Loader
%{php_pear_dir}/Symfony/Component/Routing/Matcher
